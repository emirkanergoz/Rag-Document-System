from app.data_loader import load_all
from app.rag import build_index, retrieve
from app.logic import *

sozlesme, df, guncellemeler = load_all()
index, chunks = build_index(sozlesme)

query = input("Sorunuzu yazın: ")

package = get_package(query)
intent = detect_intent(query)

if not package:
    print("Lütfen Basic, Pro veya Enterprise paketlerinden birini belirtin.")
    exit()

cevap_parcalari = []
metadata = []

# 🔹 FİYAT → CSV
if intent["price"]:
    price = get_price(df, package)
    cevap_parcalari.append(f"{package} paketinin fiyatı {price['fiyat']} TL'dir.")
    metadata.append("paket_fiyatlari.csv")

# 🔹 İADE → JSON > TXT
if intent["refund"]:
    update = get_latest_update(guncellemeler, package)

    if update:
        cevap_parcalari.append(update["degisiklik"])
        metadata.append(f"guncellemeler.json ({update['tarih']})")
    else:
        chunks_found = retrieve(query, index, chunks)
        cevap_parcalari.append(chunks_found[0])
        metadata.append("sozlesme.txt")

# 🔹 İPTAL → SADECE TXT
if intent["cancel"]:
    chunks_found = retrieve(query, index, chunks)
    cevap_parcalari.append(chunks_found[0])
    metadata.append("sozlesme.txt")

# 🔹 Eğer intent yoksa → genel
if not any(intent.values()):
    chunks_found = retrieve(query, index, chunks)
    cevap_parcalari.append(chunks_found[0])
    metadata.append("sozlesme.txt")

# 🎯 FINAL OUTPUT
print("\n--- CEVAP ---\n")
print(" ".join(cevap_parcalari))

print("\n--- REFERANSLAR ---")
for m in metadata:
    print("-", m)