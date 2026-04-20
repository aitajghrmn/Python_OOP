class User:
    def __init__ (self,name,age):
        self.name=name
        self.age=age

user1=User("Aitaj" , 21 )
user2=User("Tural" , 23)

if user1.age > user2.age:
    print(f"{user1.name} is older than {user2.name}")

else:
    print(f"{user2.name} is older than {user1.name}")
