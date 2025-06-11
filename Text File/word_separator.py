# Open the file in read mode
with open('data.txt', 'r') as file:
    # Read the file line by line
    for line in file:
        # Remove leading/trailing whitespace and split into words
        words = line.strip().split()
        # Join words with '#' and print
        print('#'.join(words))