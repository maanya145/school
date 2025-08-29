# Create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message.
import pickle

# Create binary file with one or more records
def create_file():
    with open("students.dat", "wb") as f:
        n = int(input("How many students? "))
        for _ in range(n):
            roll = int(input("Enter roll number: "))
            name = input("Enter name: ")
            pickle.dump([roll, name], f)

# Search for a roll number in the binary file
def search_roll():
    roll_no = int(input("Enter roll number to search: "))
    found = False
    try:
        with open("students.dat", "rb") as f:
            while True:
                try:
                    record = pickle.load(f)
                    if record[0] == roll_no:
                        print("Record Foundb--->","Name:", record[1])
                        found = True
                        break
                except EOFError:
                    break
        if not found:
            print("Roll number not found.")
    except FileNotFoundError:
        print("File not found. Create the file first.")

# Main
create_file()
search_roll()
