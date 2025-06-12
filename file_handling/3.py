#12/06/2025
#Program to write user input line to a file using writeline()

n = int(input("Enter the number of lines to be written: "))
lines = []
for i in range(n):
    line = input(f"Enter line {i+1}: ")
    lines.append(line + "\n")

with open("user_input.txt", "w") as f:
    f.writelines(lines)
print("All lines written to user_input.txt")