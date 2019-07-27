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

    def __cmp__(self, other):
        return (self.x > other.x) and (self.y > other.y)


class ePoint:
    def __init__(self, radius, angle):
        self.radius = radius
        self.angle = angle
        self.x = radius * math.cos(angle)
        self.y = radius * math.sin(angle)

    def cartesian(self):
        return (self.x, self.y)

    def polar(self):
        return (self.radius, self.angle)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __cmp__(self, other):
        return (self.x > other.x) and (self.y > other.y)
