class Isci:
    def __init__(self,ad,saat_basi):
        self.ad=ad
        self.saat_basi=saat_basi

class Freelancer(Isci):
    def __init__(self,ad,saat_basi,ixtisas):
        super().__init__(ad,saat_basi)
        self.ixtisas=ixtisas

    def melumat(self):
        print(f"Ad : {self.ad} " )
        print(f"Saatlik ucret : {self.saat_basi} " )
        print(f"Ixtisas : {self.ixtisas} " )

f = Freelancer("Elvin", 25, "Web Developer")
f.melumat()
