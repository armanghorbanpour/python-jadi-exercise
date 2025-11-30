def divide(a, b):
    try:
        result= a / b
        return result
    except ZeroDivisionError:
        return "Error: second number shouldn't be zero!"

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
except ValueError:
    print("Error: You should enter only integers!")
else:
    print("Result: ",divide(num1, num2))

finally:
    print("The program ran successfully")
