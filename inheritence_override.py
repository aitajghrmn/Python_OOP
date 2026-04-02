class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def describe(self):
        return "This is a car"


class ElectricCar(Car):
    def __init__(self, brand, year, battery):
        super().__init__(brand, year)
        self.battery = battery

    def describe(self):
        return "This is an electric car"


car1 = ElectricCar("Tesla", 2020, 100)

print(car1.describe())