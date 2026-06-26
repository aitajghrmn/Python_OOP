#!/usr/bin/python3

reqemler = [1, 2, 3, 4, 5]

# 1. ƏNƏNƏVİ ÜSUL (Həmişə yazdığımız)
kvadratlar_normal = []
for x in reqemler:
    kvadratlar_normal.append(x * x)

print("Normal üsul:", kvadratlar_normal) # [1, 4, 9, 16, 25]


# 2. LIST COMPREHENSION ÜSULU (Tək sətirdə möcüzə)
# Sintaksis: [ nə_etmək_istəyirəm for x in harada ]
kvadratlar_fast = [x * x for x in reqemler]

print("Sürətli üsul:", kvadratlar_fast) # [1, 4, 9, 16, 25]