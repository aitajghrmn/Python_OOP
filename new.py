'''class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Aytac", 20)

print(student1.name)
print(student1.age)'''

class CAR:
    def __init__(self , brand, year):
        self.brand =brand
        self.year=year

    def introduce(self):
        return ("This car is a " + self.brand + " from " + str(self.year) + " year.")
    


car1=CAR("Mercedes", 2016)
car2=CAR("BMW", 2018)

print(car1.brand)
print(car1.year)
print(car1.introduce())