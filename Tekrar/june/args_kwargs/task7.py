def boyuk_xercleri_topla(**kwargs):
    cem = 0
    for key , value in kwargs.items():
        if value > 100 :
            cem+= value 
    return cem


print("Yekun Böyük Xərclər:", boyuk_xercleri_topla(kommunal=120, restoran=80, kirayə=500, taksi=30))