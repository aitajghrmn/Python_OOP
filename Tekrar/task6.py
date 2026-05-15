class Animal:
    def __init__ (self,name,type):
        self.name = name
        self.type = type

    def about(self):
        print(f" My name is {self.name} and I am a {self.type}")

