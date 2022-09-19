n=int(input("enter the number of rows:"))
def numpat(n):
    num=1
if(n>0):
    for i in range(0,n):
        num=1
        for j in range(0,i+1):
            print(num,end=" ")
            num=num+1
        print(" ")
else:
    print("enter valid input")
    numpat(n)
