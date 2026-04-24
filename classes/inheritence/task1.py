class Animal :
    def __init__ (self, name):
        self.name =name 

    def speak(self):
        print(f"{self.name} makes a sound")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow")

c1 = Cat("Mestan")
c1.speak()
