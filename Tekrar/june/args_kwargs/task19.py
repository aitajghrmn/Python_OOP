def sisteme_giris(**kwargs):
    u=kwargs.get("istifadeci_adi")
    p=kwargs.get("parol")


    if u == "admin" and p == "12345" :
        print("Xoş gəldiniz, Rəis!")

    else :
        print("İstifadəçi adı və ya parol səhvdir!")


sisteme_giris(istifadeci_adi="admin", parol="12345") 
sisteme_giris(istifadeci_adi="admin") 