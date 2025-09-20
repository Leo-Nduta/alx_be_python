num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

if operation == "+":
    result = (num1+num2)
    
elif operation == "-":
    result = (num1-num2)
    
elif operation == "*":
    result = (num1*num2)
    
else:
    if num2 == 0:
        print("Cannot divide by zero.")
        result = None
    else:
        result = (num1/num2)
print("The result is", result)