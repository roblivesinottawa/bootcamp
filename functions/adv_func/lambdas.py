# the usual way of defining a function:

def square(num):
    return num * num

print(square(10)) #100

# using a lambda function.
# it is a nameless function
# it usually wont be stored in a variable

multiply = lambda num: num * num
print(multiply(20)) #400

add = lambda a, b: a + b
print(add(10, 20)) #30

divide = lambda x, y: x / y
print(divide(300, 3)) #100.0

subtract = lambda c, d: c - d
print(subtract(1000, 459)) #541 

# the usual function:
def subtract(c, d):
    return c - d

subtract(1000, 400)