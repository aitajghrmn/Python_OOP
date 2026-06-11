anbar = [
    {"mehsul": "Kofe", "miqdar": 50, "qiymet": 6},
    {"mehsul": "Cay", "miqdar": 0, "qiymet": 3},
    {"mehsul": "Sokolad", "miqdar": 20, "qiymet": 4},
    {"mehsul": "Seker", "miqdar": 0, "qiymet": 2}
]

for mehsul in anbar:
    if mehsul["miqdar"] == 0:
        print(f"{mehsul['mehsul']} anbarda bitib")