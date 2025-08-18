stack = [] # empty list

def push(item):
    stack.append(item)
    print(item, "pushed to stack")

def pop():
    if not is_empty():
        return stack.pop()
    else:
        print("stack is empty")

def is_empty():
    return len(stack) == 0

def peek():
    if not is_empty():
        return stack[-1]
    else:
        print("stack is empty")

def display():
    if is_empty():
        print("stack is empty")
    else:
        print("stack elements", stack)


