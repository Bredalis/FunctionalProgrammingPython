
# Mutando lista
def concatenacion(lista):
    lista.append("Manzana")
    return lista

lista = ["Pera", "Banana"]
print(concatenacion(lista))
print(lista)

# Lista sin mutación
def concatenacion_2(lista):
    return lista + ["Manzana"]

lista = ["Pera", "Banana"]
print(concatenacion_2(lista))
print(lista)

# Diccionario
a = {"Hola": "Amigos"}
b = {"Saludos": "Chicos"}

c = a.copy()
c.update(b)
print(c, a, b)