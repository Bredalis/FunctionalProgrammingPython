
from pyrsistent import freeze, thaw


# Initial data
data = [[1, 2, 3], [3, 4, 5], {"a": 10, "b": 20}]
print("Original Structure:\n", data)

# Freeze the structure to make it immutable
immutable_data = freeze(data)
print("\nImmutable Structure:\n", immutable_data)

# Thaw the structure to get the modifiable version
print("\nThawed Structure:\n", thaw(immutable_data))
