gelen_boy = "1.75 metrdən çox"

try :
    boy = float(gelen_boy)
    print(boy)

except ValueError :
    print("Xəta: Daxil edilən məlumat rəqəm formatında olmalıdır!")