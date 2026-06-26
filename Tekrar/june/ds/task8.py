mehsullar = [
    {"ad": "Telefon", "qiymet_usd": 800},
    {"ad": "Noatbuk", "qiymet_usd": 1200},
    {"ad": "Qulaqliq", "qiymet_usd": 100}
]

yeni_qiymet=[x["qiymet_usd"] * 1.7 for x in mehsullar ]
print(yeni_qiymet)