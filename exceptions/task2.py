try :
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))

    print(a/b)

except ValueError:
    print("Please enter a valid number.")


except ZeroDivisionError:
    print("Cannot divide by zero")
