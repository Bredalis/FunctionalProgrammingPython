
from pyrsistent import pvector, v

def actualizar(lista, valor):
	nueva_lista = lista[:]
	nueva_lista[-1] = valor

	return nueva_lista

lista = [1, 2, 3]
nueva_lista = actualizar(lista, 5)
print(nueva_lista)

vec = pvector([1, 2, 3])
vec_2 = v(1, 2, 3)

print(vec[2])
print(vec_2[0])

# Mutacion

print(vec.append(4))
print(vec)

print(vec_2.set(0, 11))
print(vec_2)