# WAP to write and read student data who got more than 80 marks
import csv

with open("students.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No.", "Name", "Marks"])
    writer.writerow([1, "Amit", 100])
    writer.writerow([2, "Sneha", 99])
    writer.writerow([3, "Rahul", 98])

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if int(row[2]) > 80:
            print(row)
