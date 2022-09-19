a=int(input("Enter number of rows :"))
for i in range(1,a+1):
    for j in range(1,i+1):
        j=j*0.1
        print('%.1f' %j,end=" ")
    print()
