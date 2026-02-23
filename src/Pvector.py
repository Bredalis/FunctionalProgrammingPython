
from pyrsistent import pvector, v

# Función para actualizar una lista (mutando una copia)
def actualizar(lista, valor):
    nueva_lista = lista[:]
    nueva_lista[-1] = valor
    return nueva_lista

# Lista de ejemplo
lista = [1, 2, 3]
nueva_lista = actualizar(lista, 5)
print(f"Lista actualizada: {nueva_lista}")

# Crear vectores inmutables
vec = pvector([1, 2, 3])
vec_2 = v(1, 2, 3)

print(f"Elemento en el índice 2 de vec: {vec[2]}")
print(f"Elemento en el índice 0 de vec_2: {vec_2[0]}")

# Mutación (recuerda que 'pvector' y 'v' son inmutables, las operaciones devuelven nuevas versiones)
print(f"\nVec después de append: {vec.append(4)}")
print(f"Vec original (sin cambios): {vec}")

print(f"\nVec_2 después de set: {vec_2.set(0, 11)}")
print(f"Vec_2 original (sin cambios): {vec_2}")