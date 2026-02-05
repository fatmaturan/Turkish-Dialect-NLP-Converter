from flask import Flask, render_template, request, jsonify
import torch
import whisper
import pandas as pd
import re
from fuzzywuzzy import fuzz, process
import os
import warnings

warnings.simplefilter("ignore", FutureWarning)

app = Flask(__name__)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("medium", device=device)

# Yöresel sözlük yükle
df = pd.read_csv("yoresel.csv", encoding="utf-8-sig")
sozluk = {str(k).strip().lower(): str(v).strip().lower() for k, v in zip(df["kelime"], df["anlam"])}

manuel_duzeltme = {
    "nörüyon": "ne yapıyorsun",
    "bakaysun": "bakıyorsun",
    "gideyrum": "gidiyorum",
    "duraysun": "duruyorsun",
    "gideysun": "gidiyorsun",
    "yapaysun": "yapıyorsun",
    "gız": "kız",
    "garı": "kadın",
    "goley": "kolay",
    "goley gelsin": "kolay gelsin",
    "geliyom": "geliyorum",
    "goyu": "kuyu",
}

def temizle_kelime(kelime):
    # Harf ve Türkçe karakter dışındakileri temizle
    return re.sub(r"[^\wçğıöşü]", "", kelime.lower())

# Basit Türkçe kök bulma (stem) fonksiyonu
def simple_stem(word):
    ekler = [
        'iyor', 'iyorum', 'iyorsun', 'iyoruz', 'iyorsunuz', 'iyorlar',
        'du', 'dü', 'dı', 'di', 'muş', 'müş', 'muşuz', 'miş', 'mişiz',
        'ca', 'ce', 'li', 'lı', 'lu', 'lü', 'den', 'dan', 'ten', 'tan',
        'e', 'a', 'ye', 'ya', 'm', 'n', 'k', 'z', 'sin', 'siniz', 'ler', 'lar'
    ]
    for ek in sorted(ekler, key=len, reverse=True):
        if word.endswith(ek) and len(word) > len(ek) + 2:
            return word[:-len(ek)]
    return word

def ceviri_yap(cumle):
    kelimeler = cumle.split()
    yeni_cumle = []
    for kelime in kelimeler:
        orijinal = kelime
        temiz = temizle_kelime(kelime)
        stem = simple_stem(temiz)

        if stem in manuel_duzeltme:
            yeni_cumle.append(manuel_duzeltme[stem])
        elif temiz in manuel_duzeltme:
            yeni_cumle.append(manuel_duzeltme[temiz])
        elif stem in sozluk:
            yeni_cumle.append(sozluk[stem])
        elif temiz in sozluk:
            yeni_cumle.append(sozluk[temiz])
        else:
            eslesme = process.extractOne(stem, sozluk.keys(), scorer=fuzz.ratio)
            if eslesme and eslesme[1] >= 85:
                yeni_cumle.append(sozluk[eslesme[0]])
            else:
                yeni_cumle.append(orijinal)
    return " ".join(yeni_cumle)

@app.route("/")
def index():
    return render_template("index.html")  # templates klasöründe index.html olmalı

@app.route("/upload_audio", methods=["POST"])
def upload_audio():
    if "audio_data" not in request.files:
        return jsonify({"error": "Ses dosyası yüklenmedi"}), 400

    audio_file = request.files["audio_data"]
    audio_path = "temp_audio.wav"
    audio_file.save(audio_path)

    try:
        result = model.transcribe(audio_path, language="tr", task="transcribe")
        text = result["text"].strip()
    except Exception as e:
        os.remove(audio_path)
        return jsonify({"error": f"Transkripsiyon hatası: {str(e)}"}), 500

    cevrilen = ceviri_yap(text)

    os.remove(audio_path)

    return jsonify({
        "shiveli": text,
        "istanbulce": cevrilen
    })

@app.route("/convert_text", methods=["POST"])
def convert_text():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Metin alınamadı"}), 400

    text = data["text"].strip()
    if not text:
        return jsonify({"error": "Boş metin gönderildi"}), 400

    cevrilen = ceviri_yap(text)

    return jsonify({
        "istanbulce": cevrilen
    })

if __name__ == "__main__":
    app.run(debug=True)
