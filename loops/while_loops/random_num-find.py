import random
number=random.randint(1,20)
q=int(input("Guess the number between 1 and 20: "))
while q!=number:
    if q>number:
        print("Too high ")
    else:
        print("Too low ")
print("Congratulations!")
