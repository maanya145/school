stack = []

def pushEven(N):
    #even number
    if N % 2 == 0:
        stack.append(N)
    else:
        print("odd number")

def popEven(EVEN):
    if len(stack) == 0:
        print("Stack empty")
    else:
        if N % 2 == 0:
            print(f"Popped element: {stack.pop()}")
        else:
            print("odd number")

