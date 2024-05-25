
# Funcion pura

def concatenacion(lista, elemento):
	return lista + [elemento]

# Funcion con efecto secundario

def concatenacion_2(lista, elemento):
	lista.append(elemento)
	return lista

# Mostrar resultado

lista = [1]

print("Resultado:", concatenacion(lista, 2))
print("Lista no ha comabiado:", lista)

print("\nResultado:", concatenacion_2(lista, 2))
print("Lista ha cambiado:", lista)