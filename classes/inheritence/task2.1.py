class Phone:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def info(self):
        return f"{self.brand} phone"
    
class SmartPhone(Phone):

    def camera(self):
        return "I have a camera"
    
samsung = SmartPhone("Samsung", "White")
print(samsung.brand)
print(samsung.info())
