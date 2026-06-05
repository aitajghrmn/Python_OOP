#/!usr/bin/python3

class InstagramProfil:
    def __init__(self,ad,email):
        self.ad=ad 
        self.email=email
        self.followers=0

    def takip_et(self):
        self.followers+=1
        print(f"{self.ad} 1 yeni takipci kazandi.Toplam : {self.followers} ")


profil1=InstagramProfil("aytac_dev" , "aytac@example.com")
profil1.takip_et()

