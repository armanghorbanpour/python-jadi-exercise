def divide(a,b):
    try:
        a=int(a)
        b=int(b)
        result= a/b
        return result
    except ZeroDivisionError:
        print("second number shouldnt be zero! ")
        return None
    except ValueError:
        print("you should enter only integer! ")
        return None
    finally:
        print("The program ran successfully")
num1=input("Enter first number: ")
num2=input("Enter second number: ")

print("Result: ", divide(num1 , num2))