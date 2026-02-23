
from pyrsistent import pvector, v


# Function to update a list (mutating a copy)
def update_list(input_list, value):
    new_list = input_list[:]
    new_list[-1] = value
    return new_list


# Example list
my_list = [1, 2, 3]
new_list = update_list(my_list, 5)
print(f"Updated list: {new_list}")

# Create immutable vectors
vec = pvector([1, 2, 3])
vec_2 = v(1, 2, 3)

print(f"Element at index 2 of vec: {vec[2]}")
print(f"Element at index 0 of vec_2: {vec_2[0]}")

# Mutation (remember 'pvector' and 'v' 
# are immutable, operations return new versions)
print(f"\nVec after append: {vec.append(4)}")
print(f"Original vec (unchanged): {vec}")

print(f"\nVec_2 after set: {vec_2.set(0, 11)}")
print(f"Original vec_2 (unchanged): {vec_2}")
