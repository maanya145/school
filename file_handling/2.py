#Write a function in python to count the number of lines in the file 'STORY.txt'

def count_lines(filename):
    f = open(filename, "r")
    count = 0
    