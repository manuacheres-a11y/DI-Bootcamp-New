import math
# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
class circle():
    def __init__(self,radius=None,diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("you must sprcify either the radius or diameter")

# Other abilities of a Circle instance:

# Compute the circle’s area
def diameter(self):
    return self.radius * 2
    
def diameter(self,value):
    self.radius / 2
    
def area(self):
    return math.pi * self.radius **2
    
# Print the attributes of the circle - use a dunder method

def __str__(self):
    return f"circle(radius={self.radius: .2f}, diameter={self.diameter: .2f}, area={self.area: .2f})"

# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them

#"""Add two circles — returns a new Circle with summed radii."""
def __add__(self,other):
    if not isinstance(other, circle):
        return NotImplemented
    return circle(radius=self.radius + other.radius)

def __eq__(self, other):
    #"""Check if two circles are equal (by radius)."""
    if not isinstance(other, circle):
        return NotImplemented
    return math.isclose(self.radius, other.radius)

def __lt__(self, other):
    #"""Compare two circles by radius (for sorting)."""
    if not isinstance(other, circle):
        return NotImplemented
    return self.radius < other.radius

def __gt__(self, other):
    #"""Compare two circles by radius (greater than)."""
    if not isinstance(other, circle):
        return NotImplemented
    return self.radius > other.radius

# Create circles
c1 = circle(radius=5)
c2 = circle(radius=6)
c3 = circle(radius=3)

# Print them
print(c1)
print(c2)
print(c3)


# Compare
print("c1 == c2:", c1 == c2)
print("c1 > c3:", c1 > c3)

# Sort circles
circles = [c1, c2, c3]
sorted_circles = sorted(circles)
print("Sorted circles by Radius:")
for c in sorted_circles:
    print(c)

import turtle

def draw_circles(circles):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    x_offset = 0

    for circle in circles:
        t.goto(x_offset, -circle.radius)  # Center each circle
        t.pendown()
        t.circle(circle.radius)
        t.penup()
        x_offset += circle.diameter + 10  # Space between circles

    turtle.done()
        

