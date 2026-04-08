num = 7
a = int(input("Enter a number: "))

while a != num:
    if a < num:
        print("Try bigger")
    else:
        print("Try smaller")
    a = int(input("Enter again: "))

print("Correct! 🎉")
