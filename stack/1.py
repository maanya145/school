# implementation of stacks using list
 
stack = [] # empty list

# push elements
stack.append(100)
stack.append(200)
stack.append(300)
print(f"stack after pushing:- {stack}")

# peek top element
print(f"Top element:- {stack[-1]}")

# pop element
print(f"Popped element:- {stack.pop()}")

# find stack
print(f"stack after popping {stack}")
