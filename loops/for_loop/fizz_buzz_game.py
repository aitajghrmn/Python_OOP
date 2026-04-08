'''1-dən 30-a qədər:

3-ə bölünürsə → "Fizz"
5-ə bölünürsə → "Buzz"
hər ikisinə bölünürsə → "FizzBuzz"
heç biri deyilsə → ədədin özü'''

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
