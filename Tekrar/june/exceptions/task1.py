#!/usr/bin/python3

def yasi_bol(yas_metni):
    try:
        yas = int(yas_metni)
        netice = 100 / yas
        print(f"Uğurlu nəticə: {netice}")
        
    except ValueError:
        print("Xəta: Zəhmət olmasa yaşınızı sözlə yox, rəqəmlə yazın!")
        
    except ZeroDivisionError:
        print("Xəta: Yaşınız 0 ola bilməz!")

print("--- 1-ci Sınaq (Düzgün data) ---")
yasi_bol("20") # Uğurlu nəticə: 5.0

print("\n--- 2-ci Sınaq (Hərf yazanda) ---")
yasi_bol("iyirmi")

print("\n--- 3-ci Sınaq (0 yazanda) ---")
yasi_bol("0") 