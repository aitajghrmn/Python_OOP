class Phone :
    def __init__(self,brand):
        self.brand=brand

    def info(self):
        return f"this phone is {brand} brand"
    
class SmartPhone(Phone):
    def camera(self):
        return "This phone can take a photo"
    
phone=Phone("Nokia")
smart=SmartPhone("Samsung")

def is_same_class(obj,a_class):
    return type(obj) is a_class

print(is_same_class(phone, Phone))
print(is_same_class(smart, SmartPhone))
print(is_same_class(smart, Phone))
