import math


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.radius = math.sqrt(self.x * self.x + self.y * self.y)
        self.angle = math.atan2(self.x, self.y)

    def cartesian_form(self):
        return (self.x, self.y)

    def polar_form(self):
        return (self.radius, self.angle)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
