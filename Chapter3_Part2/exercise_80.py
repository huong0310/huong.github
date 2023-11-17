import random

total_flips = 0
average_flips = 0

for i in range(10):
    #  0 là mặt sấp, 1 là mặt ngửa
    coin_faces = [0, 1]
    flip_count = 0
    consecutive_count = 0
    # Lặp cho đến khi có 3 mặt giống nhau liên tiếp
    while consecutive_count < 3:
        result = random.choice(coin_faces)
        flip_count = flip_count + 1
        print('H' if result == 1 else 'T', end=' ')

        # Kiểm tra xem mặt hiện tại có giống với mặt trước đó hay không
        if flip_count > 1 and result == coin_faces[-1]:
            consecutive_count = consecutive_count + 1
        else:
            consecutive_count = 1

        # Lưu mặt hiện tại vào danh sách
        coin_faces.append(result)

    total_flips = total_flips + flip_count
    average_flips = average_flips + flip_count / 10  
    print(" (",flip_count," flips )",sep="")

print("On average,",round(average_flips,1),"flips were needed.")
