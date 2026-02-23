
"""
Simple demonstration of closures in functional programming
A closure is a function that returns another function
"""

# Simple function - returns a value directly


def function_1():
    return 1


result_1 = function_1()
print(f"Direct result: {result_1}")
assert result_1 == 1
print("Test 1 passed!")


# Closure - returns a function, not a value
def function_2():
    def inner():
        return 1
    return inner  # Returns the function itself, not the result


# Get the inner function
inner_function = function_2()

# Now call the inner function to get the value
result_2 = inner_function()
print(f"Closure result: {result_2}")
assert result_2 == 1
print("Test 2 passed!")

# Key difference:
# function_1() -> returns 1 immediately
# function_2() -> returns a function, you need ()() to get 1
