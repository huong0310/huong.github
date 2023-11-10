num_sides = int(input("Nhập số cạnh của hình: "))



if 3 <= num_sides <= 10:
    if num_sides == 3:
        print("Hình có 3 cạnh là Tam giác.")
    elif num_sides == 4:
        print("Hình có 4 cạnh là Hình vuông hoặc hình chữ nhật.")
    elif num_sides == 5:
        print("Hình có 5 cạnh là Ngũ giác.")
    elif num_sides == 6:
        print("Hình có 6 cạnh là Lục giác.")
    elif num_sides == 7:
        print("Hình có 7 cạnh là Thất giác.")
    elif num_sides == 8:
           print("Hình có 8 cạnh là Bát giác.")
    elif num_sides == 9:
        print("Hình có 9 cạnh là Cửu giác.")
    elif num_sides == 10:
        print("Hình có 10 cạnh là Thập giác.")
else:
    print("Lỗi: Số cạnh nằm ngoài phạm vi hỗ trợ.")

