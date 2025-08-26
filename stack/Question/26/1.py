#A list contains following record of course details for a UNiversity: [Course_name, Fees, Duration]



univ = []

def Push_element(course):
    #fees greater than 100000
    if course[1] > 100000:
        univ.append(course)
    else:
        print("Fees is less than 100000")

def Pop_element():
    if len(univ) == 0:
        print("Underflow.")
    else:
        print(f"Popped element: {univ.pop()}")

courses = [
    ["MCA", 200000, 3],
    ["MBA", 500000, 2],
    ["BBA", 100000, 3],
    ]

for i in courses:
    Push_element(i)

print(univ)