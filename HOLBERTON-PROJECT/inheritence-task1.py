class Isci:
    def __init__(self,ad,saat_basi):
        self.ad=ad
        self.saat_basi=saat_basi

    def giris_cixis(self):
        print(f"{self.ad} ise geldi")

class Freelancer(Isci):
    def __init__(self,ad,saat_basi,ixtisas):
        super().__init__(ad,saat_basi)
        self.ixtisas=ixtisas

    def melumat(self):
        print(f"Ad : {self.ad} " )
        print(f"Saatlik ucret : {self.saat_basi} " )
        print(f"Ixtisas : {self.ixtisas} " )

    def giris_cixis(self):
        print(f"{self.ad} ise geldi")

class FullTimeEmployee(Isci):
    def __init__(self,ad,saat_basi,department):
        super().__init__(ad,saat_basi)
        self.department=department

    def melumat(self):
        print(f"Ad : {self.ad} " )
        print(f"Saatlik ucret : {self.saat_basi} " )
        print(f"Department : {self.department} " )

    def giris_cixis(self):
        print(f"{self.ad} ise geldi")

f = Freelancer("Elvin", 25, "Web Developer")
f.melumat()
f.giris_cixis()
