def Tinhchiphi(Tuoikhach):
    chiphi = 0.0
    for tuoi in Tuoikhach:
        if tuoi == '':
            break  
        tuoi = int(tuoi) 
        if tuoi <= 2:
            chiphi += 0.0
        elif 3 <= tuoi <= 12:
            chiphi += 14.0
        elif tuoi >= 65:
            chiphi += 18.0
        else:
            chiphi += 23.0
    return chiphi
Tuoikhach = []
while True:
    tuoi = input("Nhap tuoi cua khach: ")
    if tuoi == '':
        break
    Tuoikhach.append(tuoi)
chiphi = Tinhchiphi(Tuoikhach)
print("Chi phi vao cua cua nhom la: $%.2f" % chiphi)