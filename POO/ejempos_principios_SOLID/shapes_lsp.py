from abc import ABC, abstractmethod
""" 
EL principio de sustitución de Liskov establece que los subtipos deben ser 
sustituibles por los tipos base.

Este ejemplo muestra cómo se puede aplicar el principio de sustitución de Liskov.
"""
# Bad example
# class Rectangle:
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height

#     def calculate_area(self):
#         return self.__width * self.__height


# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)

#     def __setattr__(self, key, value):
#         super().__setattr__(key, value)
#         if key in ("width", "height"):
#             self.__dict__["width"] = value
#             self.__dict__["height"] = value


# Good example
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def calculate_area(self):
        return self.__side**2

def get_total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)


if __name__ == "__main__":
    rectangle = Rectangle(2, 3)
    print("Área rectángulo: ", rectangle.calculate_area())

    square = Square(2)
    print("Área cuadrado: ", (square.calculate_area()))

    print("Área total: ", get_total_area([Rectangle(10, 5), Square(5)]))