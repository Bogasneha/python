n=int(input("enter a number:"))
factorial=1
if(n<0):
    print("invalid input")
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print("factorial of" ,n,"is",factorial)

