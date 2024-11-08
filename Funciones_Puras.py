
# Función pura
def concatenacion(lista, elemento):
    return lista + [elemento]

# Función con efecto secundario
def concatenacion_2(lista, elemento):
    lista.append(elemento)
    return lista

# Mostrar resultado
lista = [1]

# Función pura: la lista original no cambia
print("Resultado:", concatenacion(lista, 2))
print("Lista no ha cambiado:", lista)

# Función con efecto secundario: la lista original se modifica
print("\nResultado:", concatenacion_2(lista, 2))
print("Lista ha cambiado:", lista)