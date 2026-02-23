
# Pure function
def concatenation(input_list, element):
    return input_list + [element]


# Function with side effect
def concatenation_2(input_list, element):
    input_list.append(element)
    return input_list


# Show result
my_list = [1]

# Pure function: original list doesn't change
print("Result:", concatenation(my_list, 2))
print("List unchanged:", my_list)

# Function with side effect: original list is modified
print("\nResult:", concatenation_2(my_list, 2))
print("List changed:", my_list)
