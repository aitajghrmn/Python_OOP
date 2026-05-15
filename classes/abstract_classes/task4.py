from abc import ABC, abstractmethod


class Shape(ABC):

    def description(self):
        return "This is a geometric shape"

    @abstractmethod
    def area(self):
        raise NotImplementedError("Child class must implement area")


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(4, 5)

print(rectangle.description())
print(rectangle.area())
