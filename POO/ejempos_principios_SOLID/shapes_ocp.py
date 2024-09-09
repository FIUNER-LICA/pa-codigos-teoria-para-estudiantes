from abc import ABC, abstractmethod
from math import pi
""" EL principio de apertura/cierre (OCP) establece que una clase debe estar 
abierta para extensión, pero cerrada para modificación.

Este ejemplo muestra cómo se puede aplicar el principio de apertura/cierre.
""" 
# 

# Bad example
# class Shape:
#     def __init__(self, shape_type, **kwargs):
#         self.__shape_type = shape_type
#         if self.__shape_type == "rectangle":
#             self.width = kwargs["width"]
#             self.height = kwargs["height"]
#         elif self.__shape_type == "circle":
#             self.radius = kwargs["radius"]

#     def calculate_area(self):
#         if self.__shape_type == "rectangle":
#             return self.width * self.height
#         elif self.__shape_type == "circle":
#             return pi * self.radius**2


# Good example
class Shape(ABC):
    def __init__(self, shape_type):
        self.__shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2


if __name__ == "__main__":
    # ejemplo uso de mal ejemplo
    rectangle = Shape("rectangle", width=10, height=5)
    print("Área rectángulo", rectangle.calculate_area())

    circle = Shape("circle", radius=5)
    print("Área círculo: ", circle.calculate_area())
