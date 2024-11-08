
from pyrsistent import pmap, m

# Crear diccionario inmutable
diccionario_inmutable = pmap({"Hola": "a todos", "Arbol": "Verde"})
print(f"Diccionario inmutable: {diccionario_inmutable}")

# Crear diccionario mutable
diccionario_mutable = m(a = 1, b = 5)
print(f"Diccionario mutable: {diccionario_mutable}")

# Acceder a valores
print(f"\nValor de 'Hola' en diccionario 1: {diccionario_inmutable["Hola"]}")
print(f"Valor de 'b' en diccionario 2: {diccionario_mutable["b"]}")

# Modificar diccionario inmutable (crea una nueva versión)
diccionario_inmutable_modificado = diccionario_inmutable.set("Arbol", "Rosado")
print(f"\nDiccionario inmutable modificado: {diccionario_inmutable_modificado}")
print(f"Diccionario original: {diccionario_inmutable}")