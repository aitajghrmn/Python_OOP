users = [
    {"name": "Ali", "age": 18},
    {"name": "Veli", "age": 23},
    {"name": "Aytac", "age": 21},
    {"name": "Murad", "age": 30}
]

count=0
for u in users:
    if u["age"]>20:
        print(u["name"])
        count+=1
        
        
print(count)
