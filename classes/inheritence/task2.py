class Animal:
    def __init__(self, name, owner, sound):
        self.name = name
        self.owner = owner
        self.sound = sound


class Dog(Animal):  
    def __init__(self, name, owner, sound, breed):
        super().__init__(name, owner, sound)  # Parent class constructor
        self.breed = breed

    def info(self):
        print(f"Adi: {self.name}")
        print(f"Sahibi: {self.owner}")
        print(f"Ses: {self.sound}")
        print(f"Cinsi: {self.breed}")



d1 = Dog("Toplan", "Aytac", "Hav hav", "Alabay")

d1.info()
