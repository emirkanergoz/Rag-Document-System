import pandas as pd
import json

def load_all():
    with open("data/sozlesme.txt", "r", encoding="utf-8") as f:
        sozlesme = f.read()

    df = pd.read_csv("data/paket_fiyatlari.csv")

    with open("data/guncellemeler.json", "r", encoding="utf-8") as f:
        guncellemeler = json.load(f)

    return sozlesme, df, guncellemeler