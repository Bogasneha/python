from statistics import mode
a=int(input("Enter a positive integer:"))
c=[]
for i in range(0,a):
      b=int(input("Enter element:"))
      c.append(b)
d=[]
d=c.copy()
m=0
for i in c:
      m+=i
print("Mean:",m//a)
c.sort()
e=a//2
for i in range(0,a):
      if(e==i):
          print("Median:",c[i])
print("Mode:",mode(d))
