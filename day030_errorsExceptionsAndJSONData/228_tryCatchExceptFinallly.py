try:
    # Try to perform division
    num = int(input("Enter a numerator: "))
    denom = int(input("Enter a denominator: "))
    result = num / denom
except ZeroDivisionError:
    # Handle division by zero error
    print("Error: Division by zero is not allowed.")
except ValueError:
    # Handle invalid input (non-integer)
    print("Error: Please enter valid integers.")
else:
    # Executes if no exception occurs
    print(f"Result: {result}")
finally:
    # Always executes
    print("Program execution completed.")