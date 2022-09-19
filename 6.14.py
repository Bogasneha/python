b=input("Enter character to be printed :")
a=int(input("Enter number of rows :"))
if(a<=0):
    print("INVALID NUMBER OF ROWS")
else:
    for i in range(1,a+1):
        for j in range(1,i+1):
            print(b,end=" ")
        print()
