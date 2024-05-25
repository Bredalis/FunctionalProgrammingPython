
from pyrsistent import freeze, thaw

datos = [[1, 2, 3], [3, 4, 5], {"a": 10, "b": 20}]
print(datos)

datos_inmutables = freeze(datos)
print(datos_inmutables)

print("Estructura Original:\n", thaw(datos_inmutables))