a=int(input("Enter a number:"))
b=[]
for i in range(0,a):
    c=int(input("Enter element:"))
    b.append(c)
print("List of elements =",b)
m=int(input("M ="))
n=int(input("N ="))
if(m<=0 or m>a or n<=0 or n>a):
    print("INVALID INPUT")
else:
    b.sort()
    for i in range(0,a):
        if(n-1==i):
            d=b[i]
    b.reverse()
    for i in range(0,a):
        if(m-1==i):
            e=b[i]
    print("Sum =",d+e)
    print("Difference =",e-d)
