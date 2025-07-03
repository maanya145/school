import csv

with open("users.csv", "w", newline='') as file:
    writer = csv.writer(file)
    # Write header row
    writer.writerows([["User ID", "Password"], ["user1", "Pass123"], ["user2", "abc456"]])
  
userID = input("Enter the user ID")
#search password for given user ID
with open("users.csv") as file:
    reader = csv.reader(file)
    found=False
    for row in reader:
        if row[0] == userID:
            print("Password  is",row[1])
            found = True
            break
    if not found:
        print("record not found!")
            
