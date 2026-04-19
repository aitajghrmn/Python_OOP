users = [
    {"name": "Ali", "age": 20},
    {"name": "Veli", "age": 25},
    {"name": "Aytac", "age": 21}
]



age20 = []

for u in users:
    if u["age"]>20:
        age20.append(u)

print(age20)
