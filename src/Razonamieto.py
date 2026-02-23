
def f1(lista):
    return [x * 2 for x in lista]

def f2(palabra):
    return [palabra]

# Abstracción de funciones
def f3(x, y):
    return f1(x) + f2(y)

# Pruebas de las funciones
print(f1([1, 2]))  # [2, 4]
print(f2("Hola"))  # ['Hola']
print(f3([3, 4], "Hola"))  # [6, 8, 'Hola']

# Verificación del razonamiento ecuacional
assert f3([3, 4], "Hola") == [6, 8, "Hola"]
print("Funcionó")