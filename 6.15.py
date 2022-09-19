try:
    a=float(input("Enter a number:"))
    c=int(a)
    if(c!=a):
        print("INVALID INPUT")
    else:
        b=0
        for i in range(1,c):
            if(c%i==0):
                b=b+i
        if(b==c):
            print("Its a Perfect Number")
        else:
            print("Its not a perfect Number")
except ValueError:
    print("INVALID INPUT")
