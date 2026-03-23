numbers = [1,2,3,4,5,6,7,8,9,10]

# 1. tek ededler
tek = []
for num in numbers:
    if num % 2 != 0:
        tek.append(num)

# 2. kvadratlar
kvadrat = []
for num in numbers:
    kvadrat.append(num * num)

# 3. 5-den boyukler
boyuk = []
for num in numbers:
    if num > 5:
        boyuk.append(num)

print("Tek:", tek)
print("Kvadrat:", kvadrat)
print("5-den boyuk:", boyuk)