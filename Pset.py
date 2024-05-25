
from pyrsistent import pset, s

set_1 = pset(["Mango", "Pera"])
print(set_1)

set_2 = s("Guineo", "Coco")
print(set_2)

# Union

frutas = set_1 | set_2
print(frutas)

# Adicionar

print(set_1.add("Melon"))
print(set_1)

# Eliminar

print(set_1.remove("Pera"))
print(set_1)