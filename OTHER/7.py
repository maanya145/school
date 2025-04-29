# Dividing two numbers

num = 0
while num != 100:
    try:
        num1 = eval(input("Enter first number: "))
        num2 = eval(input("Enter second number: "))

        num3 = num1 // num2

        print(f"The quotient is {num3}")
    except NameError:
        print("Variable not defined.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except:
        print("An error has occured.")
    finally:
        print("Done.")
