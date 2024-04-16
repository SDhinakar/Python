# class Circle:
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#         self.area=Circle.pi*radius**2

#     def circumference(self):
#         return 2*Circle.pi*self.radius
#     # def area(self,radius=8):
#     #     return Circle.pi*radius**2

# circle_1=Circle(4)
# print(circle_1.circumference())

# circle_2=Circle(6)
# print(circle_2.circumference())
# print(circle_2.area)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle_1 = Rectangle(4, 6)
print(f"Area of rectangle_1: {rectangle_1.area()}")
print(f"Perimeter of rectangle_1: {rectangle_1.perimeter()}")

rectangle_2 = Rectangle(3, 5)
print(f"Area of rectangle_2: {rectangle_2.area()}")
print(f"Perimeter of rectangle_2: {rectangle_2.perimeter()}")
