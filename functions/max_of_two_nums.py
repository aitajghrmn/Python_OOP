def max_of_two(a ,b):
    if a > b :
        return a
    else:
        return b
    
a=int(input("Enter the first number: " ))
b=int(input("Enter the second number: "))

print(f" The max of two numbers is {max_of_two(a,b)}")
