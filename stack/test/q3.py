# A list contains following record of course details for a University:
#[Course_name, Fees, Duration]

Univ = []

examplelistS = [
    ["MCA", 200000, 3],
    ["MBA", 500000, 2],
    ["BA", 100000, 3],
]

def Push_element(Univ, new_element):
    if new_element[1] > 100000:
        Univ.append(new_element)
    else:
        print("fees is less than 100000")

def Pop_element(Univ):
    if len(Univ) == 0:
        print("Stack Underflow")
    else:
        return Univ.pop()

for i in examplelistS:
    Push_element(Univ, i)
print(Univ)