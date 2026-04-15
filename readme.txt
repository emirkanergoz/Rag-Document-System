# 🧠 Hybrid RAG Doküman Sorgulama Sistemi

## 📌 Proje Hakkında

Bu proje, farklı veri formatlarını (TXT, CSV, JSON) bir araya getirerek **doğru, güncel ve bağlama uygun cevaplar üreten bir RAG (Retrieval-Augmented Generation) sistemi** geliştirmeyi amaçlamaktadır.

Sistem:
- Metin tabanlı dokümanlardan (TXT) bilgi çekebilir  
- Tablo verilerini (CSV) yapısını bozmadan okuyabilir  
- Güncellemeleri (JSON) dikkate alarak en güncel bilgiyi sunar  

---

## 🎯 Özellikler

### 🔍 Hibrit Veri Kullanımı
- `sozlesme.txt` → sözleşme ve kurallar (RAG ile aranır)
- `paket_fiyatlari.csv` → paket fiyatları (doğrudan sorgulanır)
- `guncellemeler.json` → güncellemeler (override edilir)

### 🧠 Akıllı Soru Anlama (Intent Detection)
- Fiyat
- İade
- İptal  
Sadece ilgili bilgiyi döner, gereksiz bilgi vermez

### 🔄 Dinamik Veri Yapısı
- CSV veya JSON değişirse sistem otomatik günceller
- Statik cevap üretmez

### 📊 Tablo Verisi Yönetimi
- CSV verisi RAG’e dahil edilmez
- Satır/sütun yapısı korunur

### 🕒 Güncel Bilgi Önceliği
- JSON verisi TXT’ye göre daha önceliklidir

### 📎 Metadata (Kaynak Gösterimi)
Sistem cevabı üretirken hangi dosyaları kullandığını takip eder

---

## 📂 Veri Seti Yapısı

data/
├── sozlesme.txt
├── paket_fiyatlari.csv
└── guncellemeler.json

---

## 📝 Örnek Veriler

### sozlesme.txt
Madde 4.1: İade süresi 14 gündür.

### paket_fiyatlari.csv
paket,fiyat
Basic,100
Pro,200
Enterprise,500

### guncellemeler.json
[
  {
    "tarih": "2024-06-01",
    "degisiklik": "Pro paket iade süresi 30 güne çıkarılmıştır."
  }
]

---

## ⚙️ Kurulum

### 1. Projeyi klonla
git clone https://github.com/kullaniciadi/hybrid-rag-document-system.git  
cd hybrid-rag-document-system  

### 2. Virtual environment oluştur
python -m venv venv  

### 3. Aktifleştir

Windows:
venv\Scripts\activate  

Mac/Linux:
source venv/bin/activate  

### 4. Bağımlılıkları yükle
pip install -r requirements.txt  

### 5. Çalıştır (CLI)
python main.py  

### 6. API (opsiyonel)
uvicorn main_api:app --reload  

Swagger:
http://127.0.0.1:8000/docs  

---

## 🔍 Örnek Sorgular

Pro paket fiyatı nedir?  
Basic paket iade süresi nedir?  
Pro paket fiyatı ve iptal şartları nedir?  

---

## 🧠 Sistem Mimarisi

### 1. RAG (TXT)
- Chunking yapılır
- Embedding oluşturulur
- FAISS ile benzerlik aranır

### 2. CSV (Tabular Data)
- Vektörize edilmez
- Direkt filtrelenir
- Veri bütünlüğü korunur

### 3. JSON (Override)
- En güncel veri önceliklidir
- TXT’yi override eder

### Öncelik sırası:
JSON > TXT

---

## 🧪 Test Senaryoları

- CSV fiyat değiştir → sistem anında günceller  
- JSON update ekle → en güncel veri kullanılır  
- TXT değiştir → RAG sonucu değişir  

---

## 📌 Tasarım Kararları

- CSV RAG’e dahil edilmedi (tablo bozulmaması için)
- JSON override mekanizması olarak kullanıldı
- Intent detection ile gereksiz bilgi engellendi
- Sistem tamamen dinamik çalışır

---

## ✅ Sonuç

Bu sistem:
- Farklı veri kaynaklarını entegre eder
- Güncel bilgiyi önceliklendirir
- Kullanıcıya bağlama uygun doğru cevap verir
- Gerçek RAG mimarisini simüle eder