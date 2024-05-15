def Tru(sign_a, digits_a, sign_b, digits_b):
    # Chuyển đổi mảng các chữ số thành số nguyên
    def array_to_int(sign, digits):
        num = int(''.join(map(str, digits)))
        return -num if sign else num

    # Kiểm tra tràn số
    def is_overflow(num):
        return num > 2147483647 or num < -2147483648

    # Chuyển đổi mảng thành số nguyên
    num_a = array_to_int(sign_a, digits_a)
    num_b = array_to_int(sign_b, digits_b)

    # Trừ hai số
    result = num_a - num_b

    # Kiểm tra tràn số
    if is_overflow(result):
        return [-1]

    # Chuyển kết quả trở lại thành dấu và mảng chữ số
    sign_result = 0 if result >= 0 else 1
    digits_result = [int(digit) for digit in str(abs(result))]

    return sign_result, digits_result

# Ví dụ sử dụng:
sign_a, digits_a = 0, [1, 2, 3]  # Biểu diễn số +123
sign_b, digits_b = 1, [4, 5]     # Biểu diễn số -45
result = Tru(sign_a, digits_a, sign_b, digits_b)
print(f"Kết quả: {result}")
