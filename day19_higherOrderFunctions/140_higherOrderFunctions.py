def add(a, b):
    return a + b

def calculator(a, b, function):
    return function(a, b)

print(calculator(1, 2, add))