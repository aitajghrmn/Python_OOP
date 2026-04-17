users = [
    {"name": "Ali", "age": 18},
    {"name": "Veli", "age": 23},
    {"name": "Aytac", "age": 21},
    {"name": "Murad", "age": 30}
]

filtered = []
count = 0

for u in users:
    if u["age"] > 20:
        print(u["name"])
        filtered.append(u)   # 🔥 əsas düzəliş
        count += 1

print(count)
print(filtered)
