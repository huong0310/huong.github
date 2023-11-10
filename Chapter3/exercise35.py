n=int(input("Nhap nam con nguoi:"))
if n<0: print("Khong hop le")
elif 0<=n<=2:
    s=n*10.5
    print("So nam con cho la:",s)
else:
    s=21+(n-2)*4
    print("So nam con cho la:",s)