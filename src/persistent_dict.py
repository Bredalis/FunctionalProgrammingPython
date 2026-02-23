
from pyrsistent import pmap, m


# Create immutable dictionary
immutable_dict = pmap({"Hello": "everyone", "Tree": "Green"})
print(f"Immutable dictionary: {immutable_dict}")

# Create mutable dictionary (actually still immutable in pyrsistent)
mutable_dict = m(a=1, b=5)
print(f"Mutable dictionary: {mutable_dict}")

# Access values
print(f"\nValue of 'Hello' in dictionary 1: {immutable_dict['Hello']}")
print(f"Value of 'b' in dictionary 2: {mutable_dict['b']}")

# Modify immutable dictionary (creates new version)
modified_immutable_dict = immutable_dict.set("Tree", "Pink")
print(f"\nModified immutable dictionary: {modified_immutable_dict}")
print(f"Original dictionary: {immutable_dict}")
