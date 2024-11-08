
from pyrsistent import freeze, thaw

# Datos iniciales
datos = [[1, 2, 3], [3, 4, 5], {"a": 10, "b": 20}]
print("Estructura Original:\n", datos)

# Congelar la estructura para hacerla inmutable
datos_inmutables = freeze(datos)
print("\nEstructura Inmutable:\n", datos_inmutables)

# Descongelar la estructura para obtener la versión modificable
print("\nEstructura Descongelada:\n", thaw(datos_inmutables))