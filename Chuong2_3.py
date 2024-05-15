def mang_trung_hang(matrix):
    # Duyệt qua từng cặp hàng trong ma trận
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            # Kiểm tra xem hai hàng có giống nhau không
            if matrix[i] == matrix[j]:
                return True
    return False

# Ví dụ sử dụng:
mang = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]
]

if mang_trung_hang(mang):
    print("Ma trận có ít nhất hai hàng giống nhau.")
else:
    print("Ma trận không có hai hàng nào giống nhau.")