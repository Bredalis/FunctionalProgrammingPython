
# Mutating list
def concatenation(input_list):
    input_list.append("Apple")
    return input_list


fruit_list = ["Pear", "Banana"]
print(concatenation(fruit_list))
print(fruit_list)


# List without mutation
def concatenation_2(input_list):
    return input_list + ["Apple"]


fruit_list = ["Pear", "Banana"]
print(concatenation_2(fruit_list))
print(fruit_list)


# Dictionary
a = {"Hello": "Friends"}
b = {"Greetings": "Guys"}

c = a.copy()
c.update(b)
print(c, a, b)
