def vurmalari_hesabla(*args):
    cem = 1
    for i in args :
        cem *= i
    return cem

print(vurmalari_hesabla(2, 3, 4))