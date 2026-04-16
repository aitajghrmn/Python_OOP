def get_info(person):
    return f"{person['name']} is {person['age']} years old and she lives in {person['city']} "
    
person = {
    "name" : "Aitaj",
    "age" : 20 ,
    "city" : "Khirdalan"
}

result=get_info(person)
print(result)
