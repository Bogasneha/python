a=int(input("Enter number of rows :"))
b=float(input("Enter number to be printed:"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print('%.1f' %b,end=" ")
        b=b+0.1
    print()
