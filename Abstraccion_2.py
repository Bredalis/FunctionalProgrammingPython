
def conteo(lista):
	if lista == []:
		return 0

	else:
		return 1 + conteo(lista[1:])

def sumatoria(lista):
	if lista == []:
		return 0

	else:
		return lista[0] + sumatoria(lista[1:])

print("Longitud de la lista:", conteo([1, 2, 3]))
print("Suma de los valores:", sumatoria([1, 2, 3]))

# Abstraccion

def conteo_suma(f, lista):
	if lista == []:
		return 0

	else:
		return f(lista[0]) + conteo_suma(f, lista[1:])

print("Conteo:", conteo_suma(lambda n: 1, [1, 2, 3, 4]))
print("Suma:", conteo_suma(lambda n: n, [1, 2, 3, 4]))