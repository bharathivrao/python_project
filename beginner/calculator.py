x = input("Enter a number: ")
y = int(input("Enter another number: "))
operator = input("Enter an operator (+, -, *, /): ")

try:
    result = eval(f"{x} {operator} {y}")
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"Error: {e}")
