class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class AreaCalculator:
    def calculate_area(self, rectangle):
        return rectangle.width * rectangle.height

# Uso
rectangle = Rectangle(5, 4)
calculator = AreaCalculator()
area = calculator.calculate_area(rectangle)
print(f"El área del rectángulo es: {area}")