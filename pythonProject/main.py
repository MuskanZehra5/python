# coding=utf-8
# This is a sample Python script.
import math


class Circle:
    radius = ""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = math.pi * self.radius ** 2
        return a

    def perimeter(self):
        p = math.pi * 2 * self.radius
        return p

    def printdetails(self):
        print(" Radius = {} \n Area = {} \n Parameter = {}".format(self.radius, self.area(),
                                                                  self.perimeter()))


x = Circle(7)
x.printdetails()
