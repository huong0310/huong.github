def TinhPi(n):
    pi = 3  
    mau = 2
    for i in range(n):
        pi += 4 / (mau * (mau + 1) * (mau + 2))
        if i % 2 == 0:
            pi -= 4 / (mau * (mau + 1) * (mau + 2))
        mau += 2
    return pi

Soluong = 15

for i in range(Soluong):
    Pixapsi = TinhPi(i)
    print(f"Giá trị xấp xỉ thứ {i+1} của π: {Pixapsi}")