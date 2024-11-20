for i in range(1, 101):
    divisibleBy3 = i % 3 == 0
    divisibleBy5 = i % 5 == 0
    if divisibleBy3 and divisibleBy5:
        print("FizzBuzz")
    elif divisibleBy3:
        print("Fizz")
    elif divisibleBy5:
        print("Buzz")
    else:
        print(i)