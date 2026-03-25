analyzer = []

while True:
    number = input("Enter a number (or 'q' to quit): ")

    if number == "q":
        break

    try:
        num = int(number)
        analyzer.append(num)
    except ValueError:
        print("Please enter a valid number!")

# əgər list boş deyilsə
if len(analyzer) > 0:

    # max tapmaq
    max_number = analyzer[0]

    # cüt və tək listləri
    evens = []
    odds = []

    for num in analyzer:
        # max
        if num > max_number:
            max_number = num

        # cüt / tək
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    print("All numbers:", analyzer)
    print("Max number:", max_number)
    print("Even numbers:", evens)
    print("Odd numbers:", odds)

else:
    print("No numbers entered.")