def add(number1, number2):
    return number1 + number2
def subtract(number1, number2):
    return number1 - number2
def multiply(number1, number2):
    return number1 * number2
def divide(number1, number2):
    return number1 / number2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

number1 = int(input("Number 1?: "))
for operator in operations:
    print(operator)
operator = input("Operator?: ")
number2 = int(input("Number 2?: "))

print(f"{number1} {operator} {number2} = {operations[operator](number1, number2)}")