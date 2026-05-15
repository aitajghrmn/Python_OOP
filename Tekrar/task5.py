import random
number=random.randint(1,10)

while True :
    guess=int(input("Guess the number: "))

    if guess>number:
        print("Daha az")
    elif guess<number:
        print("Daha cox")

    else:
        print("Tebrikler")

        break
