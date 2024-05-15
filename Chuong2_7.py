def Nhan(a, b):
    result = [0] * (len(a) + len(b))
    
    for i in range(len(a)-1, -1, -1):
        carry = 0
        for j in range(len(b)-1, -1, -1):
            temp = result[i + j + 1] + a[i] * b[j] + carry
            result[i + j + 1] = temp % 10
            carry = temp // 10
        result[i] += carry
    
    # Xóa các số 0 không cần thiết ở đầu kết quả
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    
    # Kiểm tra tràn số
    if len(result) > len(a) + len(b):
        return [-1]
    else:
        return result

# Ví dụ sử dụng:
a = [1, 2, 3]
b = [9, 8, 7]
print("Kết quả của a x b là:", Nhan(a, b))