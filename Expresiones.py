
# Paradigma normal
# Potenciar y dividir

def potenciar(dato):
	return dato * 2

def dividir(dato):
	return dato // 2

valores = [25, 13, 10, 1, 23, 0, 5]
resultado = []

for i in valores:
	x = dividir(potenciar(i))
	resultado.append(x)

print(resultado)

# Paradigma funcional

def operaciones(potenciar, dividir, dato = None):
	return dividir(potenciar(dato))

resultado = list(map(lambda x: operaciones(potenciar, dividir, x), valores))
print(resultado)