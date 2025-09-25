num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ")


def perform_operation(num1, num2, operation):
    if operation == "add":
        return (num1 + num2)
    elif operation == "subtract":
        return (num1 - num2)
    elif operation == "multiply":
        return (num1 * num2)
    else:
        if num2 == 0:
            return ("Undefined")
        else:
            return (num1 / num2)

result = perform_operation(num1, num2, operation)
print("Result:", result)
