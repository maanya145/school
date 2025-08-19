
N =[1,2,3,4,5,6,7]
myStack = []

def push_trail(N, myStack):
    # push last elements of N to myStack
    for i in N[-5:]:
        myStack.append(i)


def pop_one(myStack):
    # pop one element from myStack
    if not myStack:
        print("Stack Underflow")
        return None
    else:
        return myStack.pop()
    
    
def display_all(myStack):
    # display all elements of myStack without deleting them
    if not myStack:
        print('Empty Stack')
    else:
        print(myStack)

#test
print(myStack)
push_trail(N, myStack)
print(myStack)
print(pop_one(myStack))
display_all(myStack)







