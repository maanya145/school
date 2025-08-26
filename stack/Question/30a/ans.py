def push_Clr(ClrStack, new_Clr):
    # push new_Clr to ClrStack
    ClrStack.append(new_Clr)

def pop_Clr(ClrStack):
    # pop one element from ClrStack
    if len(ClrStack) == 0:
        print("Stack Underflow")
        return None
    else:
        return ClrStack.pop()
    
def isEmpty(ClrStack):
    return len(ClrStack) == 0
