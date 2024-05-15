def Tru(a, b):
    result = []
    c = 0
    len_a = len(a)
    len_b = len(b)
    max_len = len_a

    for i in range(1, max_len + 1):
        digit_a = int(a[-i])
        digit_b = int(b[-i]) if i <= len_b else 0
        diff = digit_a - digit_b - c

        if diff < 0:
            diff += 10
            c = 1
        else:
            c = 0

        result.append(diff)

    # Loại bỏ các số 0 không cần thiết từ đầu kết quả
    while result[-1] == 0 and len(result) > 1:
        result.pop()

    return result[::-1]

# Ví dụ sử dụng:
a = [7, 8, 9, 2]  # 7892
b = [3, 2, 5]     # 325
print("Kết quả của a - b là:", Tru(a, b))