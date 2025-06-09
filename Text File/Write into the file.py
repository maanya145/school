f = open("notes.txt", "w")
f.write("This is my first line.\n")
f.write("Python makes file handling easy.\n")
f.close()

with open("diary.txt", "w") as file:
    for i in range(3):
        line = input("Enter a line: ")
        file.write(line + "\n")

lines = ["First line\n", "Second line\n", "Third line\n"]

with open("sample.txt", "w") as file:
    file.writelines(lines)