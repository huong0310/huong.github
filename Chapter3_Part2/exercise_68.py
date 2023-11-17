def TinhBitchanle(Bitnhap):
    if len(Bitnhap) != 8:
        return "Loi: Chuoi phai chua 8 Bit."
    so0 = Bitnhap.count('0')
    so1 = Bitnhap.count('1')
    if (so0 + so1) % 2 == 0:
        return "Bit chan le phai la 0."
    else:
        return "Bit chan le phai la 1."
while True:
    Bitnhap = input("Nhap mot chuoi 8 Bit: ")
    if Bitnhap == '':
        break
    ketqua = TinhBitchanle(Bitnhap)
    print(ketqua)