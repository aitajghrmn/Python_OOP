#!/usr/bin/python3

def paytaxti_tap(**kwargs):
    """
    Bu funksiya gələn dağınıq məlumatların içindən 
    YALNIZ 'paytaxt' sözünü cımbızla çəkib çıxarır.
    """
    # Qutunun daxilinə dövr (for) salmırıq. Direct əlimizi atıb götürürük:
    p = kwargs.get("paytaxt")
    
    print(f"Axtarılan paytaxt: {p}")

# --- TEST MƏRHƏLƏSİ ---

# Test 1: İçində "paytaxt" olan düzgün məlumat göndəririk
print("--- Test 1 İşə düşdü ---")
paytaxti_tap(olke="Azərbaycan", paytaxt="Bakı", pul="Manat")

# Test 2: İçində "paytaxt" OLMAYAN fərqli bir məlumat göndəririk
print("\n--- Test 2 İşə düşdü ---")
paytaxti_tap(ad="Aytac", ixtisas="Backend", seher="Gəncə")