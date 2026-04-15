from fastapi import FastAPI
from app.data_loader import load_all
from app.rag import build_index, retrieve
from app.logic import *

app = FastAPI()

sozlesme, df, guncellemeler = load_all()
index, chunks = build_index(sozlesme)

@app.get("/ask")
def ask(query: str):
    package = get_package(query)
    intent = detect_intent(query)

    if not package:
        return {"error": "Paket bulunamadı"}

    cevap = []
    metadata = []

    if intent["price"]:
        price = get_price(df, package)
        cevap.append(f"{package} paketinin fiyatı {price['fiyat']} TL'dir.")
        metadata.append("paket_fiyatlari.csv")

    if intent["refund"]:
        update = get_latest_update(guncellemeler, package)

        if update:
            cevap.append(update["degisiklik"])
            metadata.append(f"guncellemeler.json ({update['tarih']})")
        else:
            chunks_found = retrieve(query, index, chunks)
            cevap.append(chunks_found[0])
            metadata.append("sozlesme.txt")

    if intent["cancel"]:
        chunks_found = retrieve(query, index, chunks)
        cevap.append(chunks_found[0])
        metadata.append("sozlesme.txt")

    if not cevap:
        chunks_found = retrieve(query, index, chunks)
        cevap.append(chunks_found[0])
        metadata.append("sozlesme.txt")

    return {
        "cevap": " ".join(cevap),
        "referanslar": metadata
    }