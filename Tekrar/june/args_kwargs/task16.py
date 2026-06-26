def rolu_yoxla(**kwargs):
    g=kwargs.get("rol" , "qonaq")

    if g == "admin" :
        print("Sisteme giris icazesi verildi")
    else:
        print("giris qadagandir")

rolu_yoxla(ad="Aytac", rol="admin") 
rolu_yoxla(ad="Emin") 