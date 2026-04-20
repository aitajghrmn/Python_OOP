class User:
    def __init__ (self,name,age):
        self.name=name
        self.age=age

user1=User("Aitaj" , 21 )
user2=User("Tural" , 23)

if user1.age>18:
    print("You are an adult")

else:
    print("You are a child")


if user2.age>18:
    print("You are an adult")

else:
    print("You are a child")
