class Person :

    def __init__(self,name):
        self.name=name

    def talk(self):
        return "I can talk"


class Student(Person):
    def study(self):
        return "I can study"
    
aytac=Student("Aytac")

print(aytac.name)
print(aytac.talk())
print(aytac.study())
