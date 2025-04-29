# Predict the output

A = 0
B = 6
print("One")

try:
    print("Two")
    X = 8 / A
    print("Three")
except ZeroDivisionError:
    print(B * 2)
    print("Four")
except:
    print(B * 3)
    print("Five")
finally:
    print("program done")
