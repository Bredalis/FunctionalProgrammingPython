
from pyrsistent import pset, s

# Crear conjuntos inmutables
set_1 = pset(["Mango", "Pera"])
print(f"Conjunto 1: {set_1}")

set_2 = s("Guineo", "Coco")
print(f"Conjunto 2: {set_2}")

# Unión de conjuntos
frutas = set_1 | set_2
print(f"\nUnión de conjuntos: {frutas}")

# Agregar un elemento al conjunto (crea una nueva versión)
set_1_modificado = set_1.add("Melon")
print(f"\nConjunto 1 después de agregar 'Melon': {set_1_modificado}")

# Eliminar un elemento del conjunto (crea una nueva versión)
set_1_modificado_2 = set_1.remove("Pera")
print(f"Conjunto 1 después de eliminar 'Pera': {set_1_modificado_2}")