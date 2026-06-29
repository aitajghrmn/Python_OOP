gelen_mebleg = "100azn"


try:
    mebleg = float(gelen_mebleg)
    print(f"Köçürülən məbləğ: {mebleg}")
except ValueError:
    print("Xəta: Məbləğ düzgün formatda deyil!")