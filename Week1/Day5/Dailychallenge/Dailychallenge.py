import math
# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
class circle():
    def __init__(self,radius,diameter):
        self.radius = radius
        self.diameter = diameter

# Other abilities of a Circle instance:

# Compute the circle’s area
def get_radius(self):
    return self.radius
    
def get_diameter(self):
    return self.diameter
    
def calc_area(self):
    return (math.pi * self.radius) **2
    
# Print the attributes of the circle - use a dunder method

def __str__(self):
    return ("f{self.radius},{self.diameter}")

# Be able to add two circles together, and return a new circle with the new radius - use a dunder method

def __compiltwocircles__(self,new_circle):
        new_radius = self.radius + new_circle.radius
        new_circle = circle(new_radius)
        return new_circle

# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them

def __compareTwoCircles__(self,other_circle):
    if self.radius > other_circle.radius:
        return True
    else:
        return False
def __isequal__(self,other_circle):
    if self.radius == other_circle.radius:
        return True
    else:
        return False
def sort(self):
    self.list_circles.append(self)
    return sorted(self.list_circles, key=lambda self: self.radius, reverse=True)
        

