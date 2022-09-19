try:
    a=int(input("Enter a binary number"),2)
    b=input("Conversion(D/O):")
    if(b=='D'):
        print("Decimal :",int(a))
    elif(b=='O'):
        print("Octal :",oct(a))
    else:
        print("INVALID CHOICE")
except ValueError:
    print("Invalid b inary number")
