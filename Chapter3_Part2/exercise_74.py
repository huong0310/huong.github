for a in range(1,11):
    print(" ",a,end="")
print("")
for b in range(1,11):
    print(b,end=" ")
    for i in range(1,11):
        print(i*b,end="  ")
    print("")