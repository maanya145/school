#Text file handling

# with open("example.txt", "r") as f:
#     print(f.read())

myfile = open("example.txt", "r")
str = myfile.readline()
print(str)
myfile.close()
