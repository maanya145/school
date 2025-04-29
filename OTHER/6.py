# WAP to ensure that integer is given as input in case other, it should display not a valid integer


try:
    x = int(input("What's x: "))
except ValueError:
    print("Not a valid integer.")
finally:
    print(f"x is {x}")
