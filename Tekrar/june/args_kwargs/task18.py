def odenis_sistemi(**kwargs):
    g=kwargs.get("kupon" , "YOXDUR")

    if g=="YAY20":
        print("20% endirim tətbiq olundu!")

    else:
        print("Kupon daxil edilməyib, tam qiymət ödənilir.")

odenis_sistemi(mebleg=100, kupon="YAY20")
odenis_sistemi(mebleg=100) # Kupon yoxdur