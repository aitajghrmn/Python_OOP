yas=int(input("Yasiniz: "))
if yas < 0:
    print("Yas menfi ola bilmez")
elif yas <13:
    print("Usag")
elif yas>13 and yas<18:
    print("Yeniyetme")
elif yas > 18 and yas <65:
    print("Yetkin")
else:
    print("Yasli")
