import pickle

FileName = "students.dat"

def write_data():
    students = []
    n = int(input("Enter the number of students: "))
    for i in range(n):
        roll = int(input("Enter the roll number: "))
        name = input("Enter the name: ")
        address = input("Enter the address: ")
        students.append((roll, name, address))
        
    # Move the file operation inside the function
    with open(FileName, "wb") as f:
        pickle.dump(students, f)

# Call the function
# write_data()


def read_data():
    try:
        with open(FileName,"rb") as f:
            students = pickle.load(f)
            for i in students:
                print(f"Roll No: {i[0]}, Name: {i[1]}, Address: {i[2]}")
    except:
        print("File not found")


def search_data():
    try:
        with open(FileName,"rb") as f:
            students = pickle.load(f)
            roll_no = int(input("Enter the roll number to search: "))
            found = False
            for i in students:
                if i[0] == roll_no:
                    print("Record found")
                    found = True
                    print(f"Roll No: {i[0]}, Name: {i[1]}, Address: {i[2]}")
                    break
    
    except:
        print("File not found")

# Main
def main():
    while True:  # Added missing colon
        print("\n Students Record Menu")
        print("1. Write Student Records")
        print("2. Display all records")  # Removed extra quotation mark
        print("3. Search Roll No.")
        print("4. Exit")
        
        choice = int(input("Enter your Choice: "))  # Added space and colon
        # Removed invalid if condition
        if choice == 1:
            write_data()
        elif choice == 2:
            read_data()
        elif choice == 3:
            search_data()
        elif choice == 4:
            print("Exit from Program")
            break
        else:
            print("Invalid Choice.")

main()
