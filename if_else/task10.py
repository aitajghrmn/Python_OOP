saat = int(input("Saati daxil et: "))

if saat >= 6 and saat <= 11:
    print("Seher")
elif saat >= 12 and saat <= 17:
    print("Gunorta")
elif saat >= 18 and saat <= 23:
    print("Axsam")
else:
    print("Gece")
