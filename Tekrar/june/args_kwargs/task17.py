def imtahan_yoxla(**kwargs):
    k=kwargs.get("bal" , 0)

    if k > 51 :
        print("Tələbə imtahandan keçdi")

    else:
        print("Tələbə kəsildi")

imtahan_yoxla(ad="Aysel", bal=75) 
imtahan_yoxla(ad="Murad") 