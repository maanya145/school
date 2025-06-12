
students = ["Aarav - 92\n", "Khushi - 88\n", "Rohan - 16\n", "Isha - 81\n", "Dev - 95/n"]

with open("student_marks.txt", "w") as f:
    f.writelines(students)
print("Data successfully written to student_marks.txt")
