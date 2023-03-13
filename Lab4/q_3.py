

class Rectangle:
    def __init__(self):
        pass

    def area(self, length, width):
        a = length * width
        print("Area of rectangle of length '{}' and width '{}' is : {}".format(length, width, a))


rect = Rectangle()
rect.area(40, 55)
