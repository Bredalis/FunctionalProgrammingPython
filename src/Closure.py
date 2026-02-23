
# Función simple que retorna 1
def funcion_1():
    return 1

f1 = funcion_1()
print(f1)

assert f1 == 1
print("Si")

# Función con cierre que retorna 1 (paradigma funcional)
def funcion_2():
    def interna():
        return 1
    return interna

f2 = funcion_2()

assert f2() == 1
print("Si")