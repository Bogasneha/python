def sumdigitsquare(n):
    sq=0;
    while (n!=0):
        digit=n%10
        sq+=digit*digit
        n=n//10
    return sq
def ishappy (n):
    s=set ()
    s.add(n)
    while (True):
        if (n==1):
            return True;
        n=sumdigitsquare (n)
        if n is s:
            return false;
n=int (input ("enter the number :"))
if (ishappy (n)):
    print ("True")
else:
    print("False")
