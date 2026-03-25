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

# ən böyük ədədi tapmaq
if len(analyzer) > 0:
    max_number = analyzer[0]

    for num in analyzer:
        if num > max_number:
            max_number = num

    print("Max number:", max_number)
else:
    print("No numbers entered.")