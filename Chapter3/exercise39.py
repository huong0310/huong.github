Jackhammer=130
Gas_lawnmower=106
Alarm_clock=70
Quiet_room=40

user_input = float(input("Nhập mức âm thanh tính bằng decibel: "))

if user_input < 0:
    print("Mức âm thanh không hợp lệ")
elif user_input < 40:
    print("Mức âm thanh thấp hơn cả tiếng Quiet room")
elif user_input == 40:
    print(f"Mức âm thanh là Quiet room")
elif user_input == 70:
    print(f"Mức âm thanh là Alarm clock")
elif user_input == 106:
    print(f"Mức âm thanh là Gas lawnmower")
elif user_input == 130:
    print("Mức âm thanh là Jackkhammer")
elif user_input > 130:
    print("Mức âm thanh cao hơn cả tiếng Jackhammer")
else:
    if 40<user_input<70:
        print("Mức âm thanh nằm giữa Quiet room và Alarm Clock")
    elif 70<user_input<106:
        print("Mức âm thanh nằm giữa Alarm Clock và Gas lawnmower")
    elif 106<user_input<130:
        print("Mức âm thanh nằm giữa Gas lawnmower và Jackhammer")
    