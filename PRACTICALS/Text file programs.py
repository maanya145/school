# Write a function AMCount() in Python, which should read each character of a text file STORY.TXT, should count and display the occurrences of alphabets A and M (including small cases a and m too). 
def AMCount():
    A, M = 0, 0
    with open("story.txt", "r") as f:
        text = f.read()
        for ch in text:
            if ch == 'A' or ch == 'a':
                A += 1
            elif ch == 'M' or ch == 'm':
                M += 1
    print("A or a:", A)
    print("M or m:", M)
AMCount()

# Write a function in python that displays the number of lines starting with ‘H’ in the file “para.txt”. 
def countH():
    lines = 0
    with open("para.txt", "r") as f:
        for line in f:
            if line.strip() != "" and line[0] == 'H':
                lines += 1
    print("No of lines starting with 'H':", lines)
countH()


# Write a method/function ISTOUPCOUNT() in python to read contents from a text file WRITER.TXT, to count and display the occurrence of the word ‘‘IS’’ or ‘‘TO’’ or ‘‘UP’’ 
def ISTOUPCOUNT():
    count = 0
    with open('WRITER.TXT', 'r') as file:
        text = file.read()

        # Convert text to uppercase and remove punctuation
        text = text.upper()

        # Split into words
        words = text.split()

        # Count occurrences
        for word in words:
            if word in ['IS', 'TO', 'UP']:
                count += 1

    print("Total occurrences of 'IS', 'TO', or 'UP':", count)

# Call the function
ISTOUPCOUNT()

