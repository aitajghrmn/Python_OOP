def hepsini_topla(*args):
    toplam = 0
    for eded in args:
        toplam += eded  # Dövr gedir, hamısını toplayır...
        
    return toplam  # <--- Dövr tam BİTDİKDƏN SONRA (sola çəkdik)

print("Cəm:", hepsini_topla(5, 10, 15, 20))