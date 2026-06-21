limit = 50

def yoxla(bal):
    if bal <= limit :
        return "siz kesildiniz"
    else:
        return "tebrikler, siz kecdiniz"
    

print(yoxla(45))