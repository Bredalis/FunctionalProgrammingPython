
def double_list(items):
    return [x * 2 for x in items]


def wrap_in_list(word):
    return [word]


# Function abstraction
def combine_operations(numbers, word):
    return double_list(numbers) + wrap_in_list(word)


# Function tests
print(double_list([1, 2]))  # [2, 4]
print(wrap_in_list("Hello"))  # ['Hello']
print(combine_operations([3, 4], "Hello"))  # [6, 8, 'Hello']

# Equational reasoning verification
assert combine_operations([3, 4], "Hello") == [6, 8, "Hello"]
print("It worked")
