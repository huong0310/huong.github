ch=str(input("nhap chuoi:"))
hc=""
for i in ch:
    hc=i+hc
if hc==ch:
    print(ch ,"la chuoi palindrome")
else:
    print(ch ,"khong la huoi palindrome")