from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class AreaCalculator:
    def calculate_area(self, shape):
        return shape.area()

# Uso
rectangle = Rectangle(5, 4)
circle = Circle(3)

calculator = AreaCalculator()

rectangle_area = calculator.calculate_area(rectangle)
circle_area = calculator.calculate_area(circle)

print(f"El área del rectángulo es: {rectangle_area}")
print(f"El área del círculo es: {circle_area:.2f}")


# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
    
#     def area(self):
#         return 0.5 * self.base * self.height

# # Uso
# triangle = Triangle(6, 4)
# triangle_area = calculator.calculate_area(triangle)
# print(f"El área del triángulo es: {triangle_area}")