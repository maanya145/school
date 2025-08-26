
# Stack implementation using a list

stack = []

def push(item):
    stack.append(item)
    print(f"{item} pushed onto stack.")

def pop():
    if not is_empty():
        item = stack.pop()
        print(f"{item} popped from stack.")
        return item
    else:
        print("Stack is empty. Cannot pop.")

def peek():
    if not is_empty():
        return stack[-1]
    else:
        print("Stack is empty. Cannot peek.")

def display():
    if not is_empty():
        print("Stack contents:", stack)
    else:
        print("Stack is empty.")

def is_empty():
    return len(stack) == 0

def menu():
    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            item = input("Enter item to push: ")
            push(item)
        elif choice == '2':
            pop()
        elif choice == '3':
            top_item = peek()
            if top_item is not None:
                print("Top item is:", top_item)
        elif choice == '4':
            display()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

