try:
    a = int(input("Birinci eded: "))
    b = int(input("Ikinci eded: "))
    print(a / b)
except ValueError:
    print("Yalniz reqem daxil et")
except ZeroDivisionError:
    print("0-a bolmek olmaz")