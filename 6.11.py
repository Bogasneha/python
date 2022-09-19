def Pow(x,n):
    d=x**n
    return d
def Add(x,n):
    d=x+n
    return d
def Sub(x,n):
    d=x-n
    return d
def Mul(x,n):
    d=x*n
    return d
def Div(x,n):
    d=x/n
    return d
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("1.Power(a,b),2.Addition (a,b),3.Subtraction(a,b),4.Multiplication (a,b),5.Division (a,b)")
c=int(input("Enter your choice:"))
if(c==1):
    print("Pow(X,N)=",Pow(a,b))
elif(c==2):
    print("Add(X,N)=",Add(a,b))
elif(c==3):
    print("Sub(X,N)=",Sub(a,b))
elif(c==4):
    print("Mul(X,N)=",Mul(a,b))
elif(c==5):
    if(b!=0):
        print("Div(X,N)=",Div(a,b))
    else:
        print("0 cant be divisible")
else:
    print("INVALID CHOICE")
