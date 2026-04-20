users = [
    {"name": "Ali", "age": 20},
    {"name": "Veli", "age": 25},
    {"name": "Aytac", "age": 21},
    {"name": "Murad", "age": 30}
]


# 1. bütün adları qaytaran funksiya
def get_names(users):
    names = []
    for u in users:
        names.append(u["name"])
    return names


# 2. yaşa görə filter edən funksiya
def filter_by_age(users, min_age):
    result = []
    for u in users:
        if u["age"] > min_age:
            result.append(u)
    return result


# 3. user axtaran funksiya
def find_user(users, name):
    for u in users:
        if u["name"] == name:
            return u
    return None


# 🔥 TEST HİSSƏSİ (print-lər burada)

print("---- ALL NAMES ----")
print(get_names(users))

print("\n---- FILTER AGE > 21 ----")
filtered = filter_by_age(users, 21)
print(filtered)

print("\n---- FIND USER ----")
user = find_user(users, "Aytac")
print(user)

print("\n---- FIND NON-EXIST USER ----")
user2 = find_user(users, "Test")
print(user2)
