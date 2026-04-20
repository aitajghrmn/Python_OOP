class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old"

    def is_adult(self):
        if self.age >= 18:
            return "Adult"
        else:
            return "Child"


user1 = User("Aitaj", 21)
user2 = User("Murad", 23)
user3 = User("Yagub", 8)
user4 = User("Nigar", 24)

users = [user1, user2, user3, user4]


# ALL NAMES
print("---- ALL NAMES ----")
for u in users:
    print(u.name)


# ADULT USERS
print("\n---- ADULT USERS ----")
for u in users:
    if u.is_adult() == "Adult":
        print(u.name)


# FIND AITAJ
print("\n---- FIND AITAJ ----")
for u in users:
    if u.name == "Aitaj":
        print(u.introduce())


# AGE > 20
print("\n---- AGE > 20 ----")
for u in users:
    if u.age > 20:
        print(u.name, u.age)
