myStack =[]

N = [1,2,3,4,5,6,7,8,9,10]

def push_trail(N, myStack):
    for i in N[-5:]:
        myStack.append(i)

#test 
# push_trail(N, myStack)
# print(myStack)

def pop_one(myStack):
    if len(myStack) == 0:
        print("Stack Underflow")
        return None
    else:
        return myStack.pop()

#test 
# pop_one(myStack)
# print(myStack)

def display_all(myStack):
    if len(myStack) == 0:
        print("Stack is empty")
    else:
        print(myStack)

        