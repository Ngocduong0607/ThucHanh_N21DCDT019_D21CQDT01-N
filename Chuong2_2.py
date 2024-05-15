def mang_tam_giac_tren(matrix):
    # Duyệt qua từng hàng của ma trận
    for i in range(1, len(matrix)):
        # Duyệt qua từng cột trong hàng, từ cột 0 đến chỉ số cột của hàng i
        for j in range(i):
            # Nếu có phần tử khác không nằm phía dưới đường chéo chính thì không phải ma trận tam giác trên
            if matrix[i][j] != 0:
                return False
    # Nếu đã duyệt qua tất cả các phần tử mà không tìm thấy phần tử khác không ở phía dưới đường chéo chính, đó là ma trận tam giác trên
    return True

# Ví dụ sử dụng:
mang = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

if mang_tam_giac_tren(mang):
    print("Ma trận trên là ma trận tam giác")
else:
    print("Ma trận trên không phải là ma trận tam giác ")
