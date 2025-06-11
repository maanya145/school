f = open("student.txt", "a")
for i in range(5):
    name = input("Enter name: ")
    f.write(name)
    f.write("\n")
f.close()
''