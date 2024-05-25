
from pyrsistent import pmap, m

diccionario_1 = pmap({"Hola": "a todos", "Arbol": "Verde"})
print(diccionario_1)

diccionario_2 = m(a = 1, b = 5)
print(diccionario_2)

print(diccionario_1["Hola"])
print(diccionario_2["b"])

print(diccionario_1.set("Arbol", "Rosado"))
print(diccionario_1)