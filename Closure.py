
def funcion_1():
	x = 1
	return x

f1 = funcion_1()
print(f1)

assert f1 == 1
print("Si")

# Paradigma Funcional

def funcion_2():
	x = 1
	def interna():
		return x

	return interna

f2 = funcion_2()

assert f2() == 1
print("Si")