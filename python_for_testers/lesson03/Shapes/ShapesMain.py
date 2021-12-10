from python_for_testers.lesson03.Shapes.Circle import Circle
from python_for_testers.lesson03.Shapes.Triangle import Triangle
from python_for_testers.lesson03.Shapes.Rectangle import Rectangle

circle = Circle(3.14, 5)
print("Circle Area:", circle.calculate_area())
triangle = Triangle(15, 6)
print("Triangle Area:", triangle.calculate_area())
rectangle = Rectangle(20, 14)
print("Rectangle Area:", rectangle.calculate_area())
