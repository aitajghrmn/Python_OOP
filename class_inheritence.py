class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


class ElectricCar(Car):
    def __init__(self, brand, year, battery):
        super().__init__(brand, year)
        self.battery = battery 



    def describe(self):
        return (self.brand + " " + "is an electric car with " + " " + str(self.battery))
    

car1=ElectricCar("Tesla",2020,100)
print(car1.brand)
print(car1.battery)
print(car1.describe())


