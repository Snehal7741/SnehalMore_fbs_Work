# Custom exception for invalid operator
class InvalidOperatorError(Exception):
    def __init__(self, msg="Invalid operator! Use one of +, -, *, /"):
        self.msg = msg
        super().__init__(self.msg)

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        raise InvalidOperatorError

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    # Check for division by zero
    if operator == '/' and num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")

    result = calculate(num1, num2, operator)
    print(f"Result: {num1} {operator} {num2} = {result}")

except ValueError:
    print("Error: Invalid number input.")
except InvalidOperatorError as e:
    print("Error:", e)
except ZeroDivisionError as e:
    print("Error:", e)
