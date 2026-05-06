'''FreelAZ — Freelancer Profili
Bir Freelancer class-ı yaz. İçində:

username — dəyişməz olsun (setter olmasın)
qiymet — saatlıq qiymət, 0-dan aşağı ola bilməz
reytinq — 1-5 arasında olmalıdır

Qaydalar:

qiymet və reytinq — getter/setter ilə
profil_goster() metodu — bütün məlumatları çap etsin'''

class Freelancer:
    def __init__(self,username,qiymet,reyting):
        self.username=username
        self.__qiymet=qiymet
        self.__reyting=reyting

    @property
    def qiymet (self):
        return self.__qiymet
    
    @property
    def reyting (self):
        return self.__reyting
    
    @qiymet.setter
    def qiymet(self,deger):
        if deger < 0 :
            print("Daxil etdiyiniz qiymete uygun netice tapilmadi")
        else:
            self.__qiymet=deger

    @reyting.setter
    def reyting(self,aralig):
        if aralig < 1 or aralig > 5:
         print("Error")        

        else:
         self.__reyting = aralig  
    
    def profil_goster(self):
       print(f"{self.username} | ${self.qiymet}/saat | ⭐{self.reyting}")

f = Freelancer("elvin_dev", 25, 4)
f.profil_goster()

f.qiymet = -10
f.reyting = 7

f.qiymet = 40
f.reyting = 5
f.profil_goster()
