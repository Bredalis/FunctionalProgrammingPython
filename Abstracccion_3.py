
def numero_mayor(numeros, mayor_actual = 0):
	if numeros == []:
		return mayor_actual

	else:
		if numeros[0] > mayor_actual:
			mayor_numero = numeros[0]

		else:
			mayor_numero = mayor_actual

	return numero_mayor(numeros[1:], mayor_numero)

print(numero_mayor([1, 5, 11, 7, 4, 9, 6]))

# Abstraccion

def reducida(f, lista, acumulador):
	if lista == []:
		return acumulador

	else:
		resultado_numerico = f(lista[0], acumulador)
		return reducida(f, lista[1:], resultado_numerico)

def mayor(lista):
	return reducida(lambda num, acumulador: num if num > acumulador else acumulador, lista, 0)

def conteo(lista):
	return reducida(lambda _, acumulador: acumulador + 1, lista, 0)

def sumatoria(lista):
	return reducida(lambda num, acumulador: num + acumulador, lista, 0)

# Mostrar resultado

print("Mayor:", mayor([3, 4, 2, 1, 1]))
print("Conteo:", conteo([3, 4, 2, 1, 1]))
print("Sumatoria:", sumatoria([3, 4, 2, 1, 1]))

def mapeo(f, lista):
	return reducida(lambda elemento, acumulador: acumulador + [f(elemento)], lista, [])

def incrementar_1(lista):
	return mapeo(lambda n: n + 1, lista)

print(incrementar_1([3, 4, 2, 1, 1]))