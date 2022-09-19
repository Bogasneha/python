a=int(input("Enter start range:"))
b=int(input("Enter end range:"))
if(a>=b or a==0 or b==0):
    print("INVALID INPUT")
else:
    print("Composite number from",a,"to",b)
    for i in range(a+1,b):
        for j in range(2,11):
            if(i%j==0):
                print(i)
                break
