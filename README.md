# 🎙️ Yöresel Ağızların Standart Türkçeye Dönüştürülmesi
### Yapay Zeka Destekli Metin Madenciliği ve Ses İşleme Projesi

Bu çalışma; Türkiye'nin farklı yörelerine ait ağız ve şivelerin, gelişmiş Doğal Dil İşleme (NLP) ve Ses İşleme teknikleri kullanılarak standart İstanbul Türkçesine dönüştürülmesini sağlayan uçtan uca bir yazılım çözümüdür. Proje, kültürel mirasın korunması ve yerel ifadelerin dijital dünyada doğru anlaşılmasını hedefler.

---

## 🏆 Akademik Başarı
* **Destek:** Bu proje, **TÜBİTAK 2209-A** (Üniversite Öğrencileri Araştırma Projeleri Destekleme Programı) kapsamında **2023 yılı 2. döneminde** kabul edilmiştir.
* **Sonuç:** Proje süreci başarıyla tamamlanmış ve **2025 Kasım** ayı itibarıyla nihai raporu verilerek "Başarılı" olarak sonuçlandırılmıştır.

---

## 🧠 Proje İçeriği ve Çalışma Mantığı

Proje, hem sesli hem de yazılı verileri işleyebilen hibrit bir yapıya sahiptir:

1.  **Ses İşleme (Speech-to-Text):** Kullanıcıdan alınan canlı ses kayıtları veya ses dosyaları, derin öğrenme tabanlı modellerle analiz edilir. Yöresel diksiyonun getirdiği farklılıklar optimize edilerek metne dönüştürülür.
2.  **Metin Madenciliği (NLP):** Elde edilen metinler, gelişmiş "Bulanık Eşleşme" (Fuzzy Matching) algoritmalarından geçer. Yerel kelimeler, binlerce kayıttan oluşan özel bir sözlük veri seti üzerinde taranır.
3.  **Anlamsal Karşılık:** Kelimeler arasındaki karakter benzerliği ve anlamsal mesafe (Levenshtein Distance) hesaplanarak, yerel ifadenin literatürdeki (Standart Türkçe) en yakın karşılığı bulunur.
4.  **Web Arayüzü:** Tüm bu işlemler, Türkiye haritası temalı, modern ve kullanıcı dostu bir web arayüzü üzerinden interaktif olarak gerçekleştirilir.

---

## 🛠️ Kullanılan Teknolojiler

* **Ses Tanıma:** OpenAI Whisper (Doğruluk oranı yüksek "Medium" modeli kullanılmıştır)
* **Doğal Dil İşleme:** FuzzyWuzzy, Levenshtein Distance Algoritmaları
* **Backend:** Python & Flask Framework
* **Veri Yönetimi:** Pandas & CSV Veri Seti
* **Frontend:** HTML5, CSS3 (Tailwind CSS), JavaScript

---

## ⚙️ Kurulum ve Kullanım

### Gereksinimler
Sisteminizde **Python 3.8+** ve ses dosyalarını işleyebilmek için **FFmpeg** yüklü olmalıdır.

1.  **Bağımlılıkları Yükleyin:**
    ```bash
    pip install flask torch whisper pandas fuzzywuzzy python-Levenshtein
    ```

2.  **Uygulamayı Başlatın:**
    ```bash
    python main_proje.py
    ```

3.  **Erişim:**
    Tarayıcınızdan `http://127.0.0.1:5000` adresine giderek projeyi test edebilirsiniz.

---



---

