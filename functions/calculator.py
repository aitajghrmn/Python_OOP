def calculator (a,b,operation):
    if operation == "add" :
        return a+b
    elif operation == "substract" :
        return a-b
    elif operation == "multiply" :
        return a*b
    elif operation == "divide" :
        return a/b
    else:
        return "Invalid operation"
    
    
a=int(input("Enter first num: "))
b=int(input("Enter second num: "))
operation=input("Enter the operation (add,substract,multiply,divide): ")
result=calculator(a,b,operation)

print(result)
