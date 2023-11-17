
decimal_number = float(input("Nhập một số thập phân: "))

# Phần Nguyên
integer_part = int(decimal_number)
result_integer = ""

# Phần Thập Phân
fractional_part = decimal_number - integer_part
result_fractional = "."

# Chuyển đổi phần nguyên thành nhị phân
while integer_part > 0:
    result_integer = str(integer_part % 2) + result_integer
    integer_part = integer_part // 2

# Chuyển đổi phần thập phân thành nhị phân
precision = 15  # Số chữ số thập phân bạn muốn xem
while fractional_part > 0 and precision > 0:
    fractional_part *= 2
    result_fractional = result_fractional + str(int(fractional_part))
    fractional_part = fractional_part - int(fractional_part)
    precision = precision - 1

result = result_integer + result_fractional
print("Biểu diễn nhị phân tương ứng: ",result)

