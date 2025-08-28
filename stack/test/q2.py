ClrStack = []

def push_Clr(ClrStack, new_Clr):
    ClrStack.append(new_Clr)

def pop_Clr(ClrStack):
    if len(ClrStack) == 0:
        print("Stack Underflow")
        return None
    else:
        return ClrStack.pop()

def isEmpty(ClrStack):
    return len(ClrStack) == 0

pop_Clr(ClrStack)
push_Clr(ClrStack, ("Yellow", 237,350))
push_Clr(ClrStack, ("Red", 237,350))
print(ClrStack)


print(pop_Clr(ClrStack))


print(isEmpty(ClrStack))