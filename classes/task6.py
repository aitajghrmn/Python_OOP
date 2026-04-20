class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        if self.age >= 18:
            return "Adult"
        else:
            return "Child"


user1 = User("Aitaj", 21)
user2 = User("Yagub", 8)

print(user1.is_adult())
print(user2.is_adult())
