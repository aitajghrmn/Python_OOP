satislar = {"Musteri1": 25, "Musteri2": 40, "Musteri3": 15, "Musteri4": 60}

umumi_cem = 0

for mehsul in satislar :
    umumi_cem += satislar[mehsul]
    ortalama = umumi_cem / len(satislar)

    print(f" Cemi satis : {umumi_cem} , ortalama sartis : {ortalama}")