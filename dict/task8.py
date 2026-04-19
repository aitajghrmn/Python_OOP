users = [
    {"name": "Ali", "age": 20},
    {"name": "Veli", "age": 25},
    {"name": "Aytac", "age": 21}
]

count = 0

for u in users:
    if u["age"] > 21:
        print(u["name"])
        count += 1

print(count)
