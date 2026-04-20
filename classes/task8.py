class User:
    def __init__ (self,name,age) :
        self.name=name
        self.age=age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old"
    
    def is_adult(self):
        if self.age >= 18 :
            return "Adult"
        
        else:
            return "Child"
        
user1=User("Aitaj" , 21 )
user2=User("Yagub" , 8)

print(user1.introduce())
print(user1.is_adult())

print()

print(user2.introduce())
print(user2.is_adult())
