#!/usr/bin/python3

istifadeci = {"ad": "Aytac", "sahə": "Backend"}

try:
    # TƏHLÜKƏLİ ZONA: Python, bura nəzarət elə, xəta çıxa bilər
    print(istifadeci["yas"])

except KeyError:
    # MÜDAFİƏ ZONASI: Əgər yuxarıda KeyError (açar tapılmadı) xətası çıxsa, bura keç
    print("Xəta: Bu istifadəçinin yaş məlumatı tapılmadı!")

# Sistem çökmədiyi üçün kod aşağıya doğru davam edə bilir:
print("Sistem işləməyə davam edir...")