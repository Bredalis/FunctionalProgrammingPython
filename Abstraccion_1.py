
def incrementar_1(numeros):
	if numeros == []:
		return []

	else:
		return [numeros[0] + 1] + incrementar_1(numeros[1:])

print("Incrementar en 1:", incrementar_1([1, 2, 3]))

def incrementar_2(numeros):
	if numeros == []:
		return numeros

	else:
		return [numeros[0] + 2] + incrementar_2(numeros[1:])

print("Incrementar en 2:", incrementar_2([1, 2, 3]))

# Abstraccion

def incrementar(f, numeros):
	if numeros == []:
		return []

	else:
		return [f(numeros[0])] + incrementar(f, numeros[1:])

print("Incrementar en 1 (Abstraccion):", incrementar(lambda x: x + 1, [1, 2, 3]))
print("Incrementar en 2 (Abstraccion):", incrementar(lambda x: x + 2, [1, 2, 3]))