numbers=[1,2,3,4,5,6,7,8,9,10]
cut=[]
for num in numbers:
    if num % 2 == 0:
        cut.append(num)

print(cut)