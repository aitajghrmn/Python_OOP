telebeler = [
    {"ad": "Aytac", "bal": 95},
    {"ad": "Məmməd", "bal": 42},
    {"ad": "Nərmin", "bal": 78}
]


statuslar = ["Keçdi" if x["bal"] >= 51 else "Kəsildi" for x in telebeler]

print(statuslar)
