#Warmup 3: Scope in Action

# Example 1: Local variable

def example_one():
    message = "Hello from inside the function!"
    print(message)

example_one()

#to access a local variable outside the function:
# print(message)

# Error:
# NameError: name 'message' is not defined


# Example 2
def example_two():
    message = "Hello from the return function!"
    return message

result = example_two()

print(result)
