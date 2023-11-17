i=1
TongHoaDon=0
print("Don gia cac san pham:")
while True:
    GiaSP=input()
    if GiaSP=="":
        break
    else:
        TongHoaDon = TongHoaDon+float(GiaSP)
        i=i+1
if TongHoaDon%5<2.5:
    CanThanhToan=TongHoaDon-(TongHoaDon%5)
elif TongHoaDon%5>=2.5:
    CanThanhToan=TongHoaDon+(5-TongHoaDon%5)     
print("Tong hoa don la: ",TongHoaDon,"\nSo tien can thanh toan la: ", CanThanhToan,sep="")
    
