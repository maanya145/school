"""def SI(P,R,T):
    return((P*R*T)/100)
SI2=SI(5000,8,2)
print(SI2)

def SI(P,R,T):
    return((P*R*T)/100)
SI2=SI(5000,12,4)
print(SI2)"""

  
'''def area(l,b):
    area=l*b
    return area
print(area(5,10))'''


#WAP to add & substract two values and return the calculated result

def calculate(x,y):
    add=x+y
    diff=x-y
    return add,diff
a,b=calculate(100,50)
print("Addition is:",a)
print("substract is:",b)

#WAP tp find factorial of a given number.
def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
for i in range(1,5):
    print(fact(i))


def interest(principal,time=2,rate=0.10):
    return principal*rate*time
prin=float(input("Enter principle amount:"))
print("Simple interest with default ROI and time values is:")
si1=interest(prin)
print("Rs.",si1)
roi=float(input("Enter rate of interest(ROI):"))
time=int(input("Enter time in years:"))
print("Simple interest with your provided ROI and time values is:")
si2=interest(prin,time,roi/100)
print("Rs.",si2)



















