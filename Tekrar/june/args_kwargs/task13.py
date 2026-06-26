def riyaziyyat_bali(**kwargs):
    # Əgər riyaziyyat yoxdursa, standart olaraq 0 qaytarsın:
    p = kwargs.get("riyaziyyat", 0)
    print(f"Riyaziyyat balı: {p}")

# Test 1: Riyaziyyat var (85 çıxmalıdır)
riyaziyyat_bali(fizika=90, riyaziyyat=85, kimya=70)

# Test 2: Riyaziyyat YOXDUR (Baxaq None çıxacaq, yoxsa 0?)
riyaziyyat_bali(fizika=90, kimya=70)