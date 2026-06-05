#!/usr/bin/python3

class Masin:
    def __init__(self,marka,model,reng):
        self.marka=marka
        self.model=model
        self.reng=reng
        self.suret=0

        def gaz_ver(self):
            self.suret+=20
            print(f"{self.model} qaz verdi.Hazirki suret : {self.suret} km/s")

class ElektrikliMasin(Masin):
    def __init__(self,marka,model,reng,batareya):
        super().__init__(marka,model,reng)
        self.batareya=batareya

    def sarj_et(self):
        print(f"{self.model} hazirda sarj olunur.Batareya faizi: {self.batareya}%")

print("---Zavod istehsala baslayir---")

masin1=Masin("Hyundai", "Elantra", "Gumusu")
masin2=ElektrikMasin("Tesla","Model Y", "Ag", 85)

print(f"1-ci masin: {masin1.marka} {masin1.model}, Rengi : {masin1.reng}")
masin1.gaz_ver()

print("\n--------------------)" 
print(f"2-ci Masin (Elektrikli) : {masin2.marka} {masin2.model}")

masin2.gaz_ver()
masin2.sarj_et()