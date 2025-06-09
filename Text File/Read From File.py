#1 Program to read entire content of a file
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

 #2 Program to read file line by line using readline()
file = open("data.txt", "r")
line = file.readline()
while line:
    print(line.strip())  # strip() removes newline characters
    line = file.readline()
file.close()

#3 Program to read all lines using readlines()
file = open("data.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()

#4  Program to count lines
file = open("data.txt", "r")
count = 0
for line in file:
    count += 1
file.close()
print("Total lines:", count)

#5  Program to count number of words
file = open("data.txt", "r")
text = file.read()
words = text.split()
print("Total words:", len(words))
file.close()

#6  Program to print lines containing a specific word
word = "computer"
file = open("data.txt", "r")
for line in file:
    if word in line:
        print(line.strip())
file.close()

#7 Program to display first N lines
N = 3
file = open("data.txt", "r")
for i in range(N):
    line = file.readline()
    if not line:
        break
    print(line.strip())
file.close()

#8  Program to count number of characters in a file
file = open("data.txt", "r")
text = file.read()
print("Total characters:", len(text))
file.close()

#9  Program to count how many times a word appears
word_to_count = "computer"
file = open("data.txt", "r")
text = file.read()
count = text.count(word_to_count)
print(f"'{word_to_count}' occurs {count} times.")
file.close()

#10 Program to print words starting with 'c'
file = open("data.txt", "r")
for line in file:
    words = line.split()
    for word in words:
        if word.startswith('c'):
            print(word)
file.close()


