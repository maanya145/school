#Write and read data from binary file
import pickle
data = {"roll": 101, "name": "Aryan", "marks": 95}
with open("student.dat", "wb") as file:
    pickle.dump(data, file)
# file.close()

with open("student.dat", "rb") as file:
    student = pickle.load(file)
    print(student)
file.close()

