ef get_older_than(users,age):
    older_users = []

    for user in users:
        if user["age"] > age:
            older_users.append(user)
    return older_users


users = [
    {"name": "Aytac", "age": 20},
    {"name": "Ali", "age": 25},
    {"name": "Nigar", "age": 22}
]
result = get_older_than(users,21)
print(result)
