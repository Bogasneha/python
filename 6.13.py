try:
    a=float(input("Enter your age:"))
    if(a<=0 or int(a)!=a):
        print("INVALID INPUT")
    else:
        b=int(a)
        if(a>=18):
            print("You are eligible to vote")
        else:
            c=0
            print("You are not eligible to vote")
            while(b>0):
                b+=1
                c+=1
                if(b==18):
                    print("you are allowed to vote after",c,"years")
                    break
except ValueError:
    print("INVALID INPUT")
