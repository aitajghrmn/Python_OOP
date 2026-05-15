from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        raise NotImplementedError("Child class must implement make_sound")


class Dog(Animal):

    def make_sound(self):
        return "HAV HAV"


dog = Dog()

print(dog.make_sound())
