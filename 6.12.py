a=int(input("Enter number of list:"))
b=[]
c=0
p=0
for i in range(a):
    c=int(input("Enter element:"))
    b.append(c)
for i in b:
    if(i%2!=0):
        p+=1
c=a-p
print("Composite number:",c)
print("Prime number:",p)
