def kesileni_tap(**kwargs):
    for acar , deyer in kwargs.items():
        if deyer < 51 :
            print(f"{acar} kesildi " )

kesileni_tap(Aysel= 85 , Eli= 42 , Leyla= 90 , Murad= 38)