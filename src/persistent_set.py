
from pyrsistent import pset, s


# Create immutable sets
set_1 = pset(["Mango", "Pear"])
print(f"Set 1: {set_1}")

set_2 = s("Banana", "Coconut")
print(f"Set 2: {set_2}")

# Union of sets
fruits = set_1 | set_2
print(f"\nUnion of sets: {fruits}")

# Add an element to the set (creates a new version)
modified_set_1 = set_1.add("Melon")
print(f"\nSet 1 after adding 'Melon': {modified_set_1}")

# Remove an element from the set (creates a new version)
modified_set_1_2 = set_1.remove("Pear")
print(f"Set 1 after removing 'Pear': {modified_set_1_2}")
