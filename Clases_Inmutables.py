
from pyrsistent import PClass, field

class Punto(PClass):
    x = field()
    y = field()

    def traslacion(self, dx, dy):
        return self.set(x = self.x + dx, y = self.y + dy)

punto_1 = Punto(x = 1, y = 2)
punto_2 = punto_1.traslacion(5, 5)

print(punto_1)
print(punto_2)

try:
    punto_1.w = 5
except AttributeError as e:
    print(e)