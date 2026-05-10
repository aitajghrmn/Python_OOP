class Animal :
    def __init__ (self,name) :
        self.name = name
    def speak (self):
        return "Animal is speaking "
    
cat=Animal("Mestan")
dog1 = Animal("Max")
dog2 = Animal("Leo")


print(dog1.name)
print(dog2.name)
print(cat.name)
print(cat.speak())
