def detect_intent(query):
    query = query.lower()

    intent = {
        "price": False,
        "refund": False,
        "cancel": False
    }

    if any(word in query for word in ["fiyat", "ücret", "price"]):
        intent["price"] = True

    if any(word in query for word in ["iade", "geri ödeme"]):
        intent["refund"] = True

    if any(word in query for word in ["iptal", "cancel"]):
        intent["cancel"] = True

    return intent


def get_package(query):
    query = query.lower()

    if "pro" in query:
        return "Pro"
    elif "basic" in query:
        return "Basic"
    elif "enterprise" in query:
        return "Enterprise"

    return None


def get_price(df, package):
    row = df[df["paket"].str.lower() == package.lower()]
    return row.to_dict(orient="records")[0] if not row.empty else None


def get_latest_update(guncellemeler, package):
    filtered = [
        g for g in guncellemeler
        if package.lower() in g["degisiklik"].lower()
    ]

    if not filtered:
        return None

    filtered.sort(key=lambda x: x["tarih"], reverse=True)
    return filtered[0]