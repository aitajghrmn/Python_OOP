class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user1 = User("Aitaj", 21)
user2 = User("Tural", 23)


if user1.age >= 18:
    print(user1.name, "is Adult")
else:
    print(user1.name, "is Child")


if user2.age >= 18:
    print(user2.name, "is Adult")
else:
    print(user2.name, "is Child")
