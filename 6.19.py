a=float(input("Enter the marks in python :"))
b=float(input("Enter the marks in c programming :"))
c=float(input("Enter the marks in Mathematics :"))
d=float(input("Enter the marks in Physics :"))
if(a<0 or a>100 or b<0 or b>100 or c<0 or c>100 or d<0 or d>100 ):
    print("INVALID MARKS")
else:
    e=a+b+c+d
    f=e/4
    print("Total :",e)
    print("Aggregate :",f)
    if(f>=75):
        print("Distinction")
    elif(f>=60 and f<75):
        print("First Division")
    elif(f>=50 and f<60):
        print("Second Division")
    elif(f>=40 and f<50):
        print("Third Division")
    else:
        print("Fail")
