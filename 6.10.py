from math import gcd

if h == "2":
    while True:
        def lcm(x, y, z):
            a = gcd(x, y, z)
            num = x
            num2 = y * z // a
            LCM = num * num2 // a

            return LCM

        x = int(input("Number 1: "))
        y = int(input("Number 2: "))
        z = int(input("Number 3: "))
        print("The LCM Of " + str(x) + " And " + str(y) + " And " + str(z) +         " Is " + str(lcm(x, y, z)))

if h == "1":
    while True:
        def lcm(x, y):
            a = gcd(x, y)
            num = x
            num2 = y
            LCM = num * num2 // a

            return LCM
        x = int(input("Number 1: "))
        y = int(input("Number 2: "))
        print("The LCM Of " + str(x) + " And " + str(y) + " Is " + str(lcm(x, y)))
