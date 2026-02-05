# 🎙️ Yöresel Ağızların Standart Türkçeye Dönüştürülmesi  
### Yapay Zeka Destekli Metin Madenciliği ve Ses İşleme Projesi

Bu proje, Türkiye’nin farklı yörelerine ait ağız ve şiveleri **standart İstanbul Türkçesine** dönüştürmeyi amaçlayan,  
**ses işleme** ve **doğal dil işleme (NLP)** tekniklerini bir arada kullanan web tabanlı bir uygulamadır.

Proje, kültürel mirasın dijital ortama aktarılmasını ve yöresel ifadelerin akademik çalışmalarda kullanılabilir hale getirilmesini hedeflemektedir.

---

## 🏆 Akademik Bilgi

- **Destek Programı:** TÜBİTAK 2209-A  
- **Kabul Dönemi:** 2023 / 2. Dönem  
- **Durum:** 2025 Kasım ayında  başarıyla sonuçlanmıştır

---

## 🧠 Çalışma Prensibi

Uygulama iki farklı şekilde çalışır:

### 🎤 Ses ile Çeviri
1. Kullanıcı mikrofon aracılığıyla ses kaydı alır  
2. Ses, **OpenAI Whisper** modeli ile metne dönüştürülür  
3. Elde edilen şiveli metin, yöresel sözlük ve NLP algoritmaları ile analiz edilir  
4. Standart Türkçe karşılığı üretilir  

### 📝 Metin ile Çeviri
- Kullanıcı doğrudan metin girer  
- Metin, yöresel kelime veri seti üzerinde taranır  
- En uygun İstanbul Türkçesi karşılığı bulunur  

---

## 🛠️ Kullanılan Teknolojiler

### 🔊 Ses İşleme
- **OpenAI Whisper (Medium model)**
- **PyTorch**
- **FFmpeg**

### 🧠 Doğal Dil İşleme (NLP)
- **FuzzyWuzzy** (Bulanık eşleşme)
- **Levenshtein Distance**
- Basit kök bulma (rule-based stemming)

### 🧩 Backend
- **Python**
- **Flask**

### 📊 Veri Yönetimi
- **Pandas**
- CSV tabanlı özel yöresel kelime veri seti

### 🎨 Frontend
- **HTML5**
- **Tailwind CSS (CDN)**
- **JavaScript**
- Web Audio API & MediaRecorder

---

## 📦 GitHub’a Dahil Edilmeyen Dosyalar

Depo boyutunu kontrol altında tutmak ve lisans kısıtları nedeniyle aşağıdaki dosyalar **bilerek repoya eklenmemiştir**:

- Whisper model ağırlıkları (`.pt`)
- Geçici ses dosyaları (`.wav`, `.mp3`)
- IDE yapılandırma dosyaları (`.idea/`)
- Sanal ortam klasörleri (`venv/`)
- Cache dosyaları (`__pycache__/`)

> Bu dosyaların GitHub’da yer almaması, projenin çalışmasını engellemez.

---

## 🧠 Yapay Zeka Modeli Hakkında

- Kullanılan model: **OpenAI Whisper – Medium**
- Model dosyaları repoya dahil edilmemiştir
- **Uygulama ilk çalıştırıldığında**, model sistemde mevcut değilse  
  **internet bağlantısı olması durumunda otomatik olarak indirilmektedir**

Alternatif olarak şu modeller de kullanılabilir:
- `tiny`
- `base`
- `small`
- `medium` (önerilen)

---

## ⚙️ Kurulum ve Çalıştırma

### Gereksinimler
- Python **3.8+**
- FFmpeg

### Gerekli Kütüphaneler
```bash
pip install flask torch whisper pandas fuzzywuzzy python-Levenshtein
