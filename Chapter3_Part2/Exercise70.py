def Mahoacaesar(thongbao, dichchuyen):
    mahoa = ''
    for kytu in thongbao:
        if kytu.isalpha():
            if kytu.islower():
                mahoa += chr((ord(kytu) - ord('a') + dichchuyen) % 26 + ord('a'))
            else:
                mahoa += chr((ord(kytu) - ord('A') + dichchuyen) % 26 + ord('A'))
        else:
            mahoa += kytu
    return mahoa
def Giaimacaesar(thongbao, dichchuyen):
    return Mahoacaesar(thongbao, -dichchuyen)
thongbao = input("Nhập thông điệp: ")
dichchuyen = int(input("Nhập số lượng dịch chuyển: "))
TBmahoa = Mahoacaesar(thongbao, dichchuyen)
TBgiaima = Giaimacaesar(TBmahoa, dichchuyen)
print("Thông điệp đã mã hóa:", TBmahoa)
print("Thông điệp đã giải mã:", TBgiaima)