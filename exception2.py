try:
    a = int(input("Birinci eded: "))
    b = int(input("Ikinci eded: "))

    if b == 0:
        print("0-a bolmek olmaz")
    else:
        result = a / b
        print("Netice:", result)

except ValueError:
    print("Yalniz reqem daxil et")

finally:
    print("Program bitdi")