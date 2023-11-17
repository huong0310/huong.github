# Nhập số nhị phân từ người dùng
binary_number = input("Nhập một số nhị phân: ")

# Kiểm tra xem đầu vào có phải là số nhị phân hay không
if not all(bit in '01' for bit in binary_number):
    print("Lỗi: Đầu vào không phải là số nhị phân hợp lệ.")
else:
    # Chuyển số nhị phân sang số thập phân
    decimal_number = int(binary_number, 2)

    # Hiển thị kết quả
    print(f"Số thập phân tương đương: {decimal_number}")
