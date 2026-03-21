numbers = []

# 5 eded al
for i in range(5):
    num = int(input("Eded daxil et: "))
    numbers.append(num)

# ilkin qiymetler
max_num = numbers[0]
min_num = numbers[0]
total = 0

# hesablamalar
for num in numbers:
    if num > max_num:
        max_num = num

    if num < min_num:
        min_num = num

    total += num

# neticeler
print("Max:", max_num)
print("Min:", min_num)
print("Sum:", total)