def get_info(person):
    return f"{person['name']} is {person['age']} years old"


person = {
    "name": "Aytac",
    "age": 21,
    "city": "Khirdalan"
}

result = get_info(person)

print(result)
