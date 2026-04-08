import random

number = random.randint(1, 20)
attempts = 5
count = 0

print("Guess the number between 1 and 20")
print("You have 5 attempts")

while count < attempts:
    q = int(input("Enter your guess: "))
    count += 1

    if q == number:
        print("Congratulations! 🎉")
        print("You guessed it in", count, "tries")
        break
    elif q > number:
        print("Too high")
    else:
        print("Too low")

    print("Remaining attempts:", attempts - count)

else:
    print("Game Over ❌")
    print("The correct number was:", number)
