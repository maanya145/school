stack ==[]

N = [1,2,3,4,5,6,7,8,9,10]

def pushEven(N):
    if N % 2 == 0:
        stack.append(N)
    else:
        print("Not Even.")

def popEven(EVEN):
    if len(EVEN) == 0:
        print("Stack Underflow")
    else:
        for i in range(len(EVEN)):
            print(EVEN.pop())
        print("Stack Empty")
