
"""
Simple immutable Point using pyrsistent
"""

from pyrsistent import PClass, field


class Point(PClass):
    x = field()
    y = field()

    def move(self, dx, dy):
        """Move the point and return a new one"""
        return self.set(x=self.x + dx, y=self.y + dy)


# Create a point
p1 = Point(x=1, y=2)
print(f"Original: {p1}")

# Move it (creates new point, original doesn't change)
p2 = p1.move(5, 5)
print(f"Moved: {p2}")
print(f"Original still: {p1}")

# Try to change it (will fail)
try:
    p1.x = 10
except AttributeError:
    print("Cannot change! Point is immutable.")
