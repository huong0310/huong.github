i=1
S=0
while True:
    n=int(input("n="))
    if i==1 and n==0:
        print("Nhap gia tri lon hon 0")
    elif n!=0:
        S=S+n
        
        i=i+1
    elif n==0:
        break
print("Gia tri trung binh la:",S/(i-1))
        
