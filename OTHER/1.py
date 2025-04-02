#WAP to calculate the compute the area of a rectangle

def area(length,breadth):
    area=length*breadth
    # print("The area of the rectangle is",area)
    return area

l=float(input("Enter the length of the rectangle:   "))
b=float(input("Enter the breadth of the rectangle:  "))   
area=area(l,b)
print("The area of the rectangle is",area)

