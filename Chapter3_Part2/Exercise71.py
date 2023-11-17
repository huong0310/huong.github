x=int(input("x="))
d=x/2
while abs(d*d-x)>(10**(-12)):
    d=(d+x/d)/2
    print(d)