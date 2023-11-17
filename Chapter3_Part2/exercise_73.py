a=str(input("nhap chuoi:"))
ch=a.replace(" ","")
hc=""
for i in ch:
    hc=i+hc
if hc==ch:
    print(a ,"la chuoi palindrome")
else:
    print(a ,"khong la huoi palindrome")