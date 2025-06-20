#convert no. of records in the binary file:
import pickle count = 0 
with open("students.dat","rb") as file:
    try:
        while True:
            record=pickle.load(file)
            count+=1
    except EOFError:
        pass
print("Total numbers of counts", count)
