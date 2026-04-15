# Hybrid RAG Doküman Sorgulama Sistemi

## 📌 Proje Hakkında

Bu proje, farklı veri formatlarını (TXT, CSV, JSON) bir araya getirerek **doğru, güncel ve bağlama uygun cevaplar üreten bir RAG (Retrieval-Augmented Generation) sistemi** geliştirmeyi amaçlamaktadır.

Sistem:

* Metin tabanlı dokümanlardan (TXT) bilgi çekebilir
* Tablo verilerini (CSV) yapısını bozmadan okuyabilir
* Güncellemeleri (JSON) dikkate alarak en güncel bilgiyi sunar

---

## 🎯 Özellikler

* 🔍 **Hibrit Veri Kullanımı**

  * `sozlesme.txt` → sözleşme ve kurallar (RAG ile aranır)
  * `paket_fiyatlari.csv` → paket fiyatları (doğrudan sorgulanır)
  * `guncellemeler.json` → güncellemeler (override edilir)

* 🧠 **Akıllı Soru Anlama (Intent Detection)**

  * Kullanıcının ne sorduğunu analiz eder:

    * Fiyat
    * İade
    * İptal
  * Sadece ilgili bilgiyi döner (gereksiz bilgi vermez)

* 🔄 **Dinamik Veri Yapısı**

  * CSV veya JSON dosyasında değişiklik yapılırsa sistem otomatik olarak güncel veriyi kullanır
  * Statik cevap üretmez

* 📊 **Tablo Verisi Yönetimi**

  * CSV verisi RAG’e dahil edilmez
  * Satır/sütun yapısı korunarak doğrudan filtrelenir

* 🕒 **Güncel Bilgi Önceliği**

  * JSON dosyasındaki en güncel kayıtlar, TXT verisinin önüne geçer

* 📎 **Metadata (Kaynak Gösterimi)**

  * Sistem, cevabı üretirken hangi dosyaları kullandığını belirtir

---

## 📂 Veri Seti Yapısı

```bash
data/
├── sozlesme.txt
├── paket_fiyatlari.csv
└── guncellemeler.json
```

### Açıklamalar

* **sozlesme.txt**
  Sözleşme maddelerini içerir.
  Örnek:
  `Madde 4.1: İade süresi 14 gündür.`

* **paket_fiyatlari.csv**
  Paket bilgilerini içerir.
  Örnek:

```csv
paket,fiyat
Basic,100
Pro,200
Enterprise,500
```

* **guncellemeler.json**
  Zamanla yapılan değişiklikleri içerir.
  Örnek:

```json
[
  {
    "tarih": "2024-06-01",
    "degisiklik": "Pro paket iade süresi 30 güne çıkarılmıştır."
  }
]
```

---

## ⚙️ Kurulum ve Çalıştırma

### 1. Projeyi klonla

```bash
git clone https://github.com/kullaniciadi/hybrid-rag-document-system.git
cd hybrid-rag-document-system
```

---

### 2. Virtual environment oluştur

```bash
python -m venv venv
```

Aktifleştir:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Bağımlılıkları yükle

```bash
pip install -r requirements.txt
```

---

### 4. Uygulamayı çalıştır (CLI)

```bash
python main.py
```

---

### 5. API olarak çalıştır (opsiyonel)

```bash
uvicorn main_api:app --reload
```

Tarayıcı:

```
http://127.0.0.1:8000/docs
```

---

## 🔍 Örnek Sorgular

```text
Pro paket fiyatı nedir?
```

```text
Basic paket iade süresi nedir?
```

```text
Pro paket fiyatı ve iptal şartları nedir?
```

---

## 🧠 Sistem Mimarisi

### 1. RAG (TXT Verisi)

* `sozlesme.txt` parçalanır (chunking)
* Sentence Transformers ile embedding oluşturulur
* FAISS ile benzerlik araması yapılır

---

### 2. CSV Yönetimi (Tabular Data)

* CSV verisi **vektörize edilmez**
* Doğrudan filtreleme yapılır

📌 **Sebep:**
Chunking işlemi tablo yapısını bozacağı için veri bütünlüğü korunmuştur.

---

### 3. JSON Güncelleme Mekanizması

* JSON verisi kontrol edilir
* Eğer ilgili paket için güncel kayıt varsa:
  → TXT verisinin yerine kullanılır

📌 **Öncelik sırası:**

```
JSON > TXT
```

---

### 4. Intent Detection

Kullanıcının sorusu analiz edilir:

* "fiyat" → CSV
* "iade" → JSON / TXT
* "iptal" → TXT

---

### 5. Hibrit Cevap Üretimi

Sistem:

* Gerekli kaynakları seçer
* Verileri birleştirir
* Tek ve anlamlı bir cevap üretir

---

## 🧪 Test ve Değerlendirme

Sistem, statik değil dinamik çalışacak şekilde tasarlanmıştır.

### Test Senaryoları:

* CSV dosyasındaki fiyatı değiştirin
  → Cevap değişmelidir

* JSON dosyasına yeni kayıt ekleyin
  → Sistem en güncel veriyi kullanmalıdır

Örnek:

```json
{
  "tarih": "2025-01-01",
  "degisiklik": "Basic paket iade süresi 7 güne düşürülmüştür."
}
```

---

## 📌 Önemli Tasarım Kararları

* CSV verisi RAG’e dahil edilmemiştir
* JSON verisi override mekanizması olarak kullanılmıştır
* Intent detection ile gereksiz bilgi verilmesi engellenmiştir
* Sistem tamamen dinamik çalışacak şekilde geliştirilmiştir

---

## ✅ Sonuç

Bu sistem:

* Farklı veri kaynaklarını entegre eder
* Güncel bilgiyi önceliklendirir
* Kullanıcıya doğru ve bağlama uygun cevap verir

---
