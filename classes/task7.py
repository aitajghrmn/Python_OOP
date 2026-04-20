class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def is_adult(self):
        if self.age >= 18:
            return "Adult"
        else:
            return "Child"
        
    def introduce(self):
        return f"hello, my name is {self.name} and i am {self.age} years old"

user1=User("Aitaj" , 21)
user2=User("Yagub" , 8)

print(user1.name,"is" , user1.is_adult())
print(user1.introduce())
