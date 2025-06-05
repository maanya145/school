# fh = open("demo.txt", "r")
# val = fh.readline()
# val1 = fh.readlines()
# print(val)
# print(val1)
# fh.close()


# fh = open("demo.txt", "r")
# for line in fh:
#     print(line)

myfile = open("demo.txt", "r")
Str = " "
size = 0
tsize = 0
while Str:
    Str = myfile.readline()
    tsize += len(Str)
    size += len(Str)
print(size)
print(tsize)
myfile.close()
