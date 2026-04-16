def get_all_names(users):
    names = []

    for user in users:
        names.append(user["name"])

    return names


users = [
    {"name": "Aytac", "age": 20},
    {"name": "Ali", "age": 25},
    {"name": "Nigar", "age": 22}
]

result = get_all_names(users)

print("Names:", result)
