#Viết chương trình tính và in lên màn hình giá bán của các mặt hàng với công thức sau
Gia_nhap=int(input("Nhap Gia niem yet: "))
Chiet_khau=int(input("Nhap Chiet khau: "))
Gia_ban=Gia_nhap-Chiet_khau+(Gia_nhap-Chiet_khau)*0.01
print("Gia ban:",Gia_ban)