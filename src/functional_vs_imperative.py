
# Normal paradigm - Power and divide
def power(data):
    return data * 2


def divide(data):
    return data // 2


values = [25, 13, 10, 1, 23, 0, 5]
result = [divide(power(i)) for i in values]

print(result)


# Functional paradigm
def operations(power_func, divide_func, data):
    return divide_func(power_func(data))


result = list(map(lambda x: operations(power, divide, x), values))
print(result)
