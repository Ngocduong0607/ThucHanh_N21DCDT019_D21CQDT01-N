def NhomCot(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if all(matrix[row][i] == matrix[row][j] for row in range(len(matrix))):
                # Tạo một danh sách để lưu trữ chỉ mục của các cột giống nhau
                group = [i, j]
                print("Nhóm cột giống nhau:", group)

# Ví dụ sử dụng:
# Định nghĩa một ma trận vuông
matrix = [
    [1, 2, 1, 2],
    [4, 5, 4, 5],
    [7, 8, 7, 8],
    [10, 11, 10, 11]
]

# In ra nhóm chỉ mục cột của các cột giống nhau
NhomCot(matrix)