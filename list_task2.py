numbers=[1,2,3,4,5,6,7,8,9,10]
cut=[]
bes_boyuk=[]

for num in numbers:
    if num % 2 == 0 :
        cut.append(num)

    if num > 5 :
        bes_boyuk.append(num)

print("5-den boyukler: " , bes_boyuk)
print("cut ededler: "  ,cut)
