
def f1(lista):
	return [x * 2 for x in lista]

def f2(palabra):
	return [palabra]

# Abstraccion

def f3(x, y):
	return f1(x) + f2(y)

print(f1([1, 2]))
print(f2("Hola"))
print(f3([3, 4], "Hola"))

# Verificacion del razonamiento ecuacional

assert f3([3, 4], "Hola" == [6, 8, "Hola"])
print("Funciono")