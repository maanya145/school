import csv

data = [
    ["sigmaland", 45075873, 4000, 30000],
    ["Joyland", 45075873, 4000, 30000],
    ["Happyland", 600000, 7000, 5000],
    ["Smilyland", 800000, 7000, 5000],
]

with open("Happiness.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


print("Happiness.csv file is created successfully")
with open("Happiness.csv") as file:
    reader = csv.reader(file)
    for i in reader:
        p = int(i[1])
        if p > 50000000:
            print(i)
with open("Happiness.csv", "r") as file:
    reader = csv.reader(file)
    count = 0
    for i in reader:
        count += 1
    print('Total number of records', count)
    
