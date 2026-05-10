class Device:
    def __init__(self,name):
        self.name=name

    def turn_on(self):
        return "The device is turned on"
    

class Laptop(Device):
    def code(self):
        return "You can code with this PC"
    
macbook=Laptop("Macbook M5")

print(macbook.turn_on())
print(macbook.code())
