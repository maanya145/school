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
        print(row)

        