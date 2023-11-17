n=int(input("n="))
m=int(input("m="))
d=int(input("d="))
while n%d!=0 and m%d!=0:
    d=d-1
print(d, "la uoc chung lon nhat")