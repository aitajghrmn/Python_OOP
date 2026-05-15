grades = {
    "Ali": 85,
    "Aytac": 95,
    "Leyla": 70
}

# bütün tələbələri və qiymətlərini göstərsin
for key, value in grades.items():
    print(key, value)

# ən yüksək qiyməti tapsın
en_yuksek = max(grades, key=grades.get)

# orta qiyməti hesablasın
ortalama = sum(grades.values()) / len(grades)

# istifadəçidən tələbə adı alıb onun qiymətini göstərsin
telebe = input("Adi daxil et: ")

if telebe in grades:
    print(telebe + ":", grades[telebe])
else:
    print("Siyahida bele telebe yoxdur")

print("En yuksek qiymet alan telebe:", en_yuksek)
print("Onun qiymeti:", grades[en_yuksek])
print("Ortalama:", ortalama)
