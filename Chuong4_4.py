class Solution:
    def HauTo(self, bt):
        # Hàm để kiểm tra xem một ký tự có phải là toán tử hay không
        def la_toan_tu(char):
            return char in '+-*/'

        # Hàm để xác định độ ưu tiên của một toán tử
        def do_uu_tien(toan):
            if toan == '+' or toan == '-':
                return 1
            elif toan == '*' or toan == '/':
                return 2
            return 0  # Giả sử các toán tử còn lại có độ ưu tiên là 0

        hau_to = []  # Danh sách lưu trữ biểu thức hậu tố
        toan_tu_stack = []  # Stack lưu trữ các toán tử

        i = 0
        while i < len(bt):
            # Bỏ qua khoảng trắng
            if bt[i] == ' ':
                i += 1
                continue

            # Nếu là toán hạng, thêm vào danh sách biểu thức hậu tố
            elif bt[i].isdigit():
                operand = ''
                while i < len(bt) and bt[i].isdigit():
                    operand += bt[i]
                    i += 1
                hau_to.append(operand)

            # Nếu là dấu mở ngoặc, đẩy vào stack toán tử
            elif bt[i] == '(':
                toan_tu_stack.append(bt[i])

            # Nếu là dấu đóng ngoặc, pop các toán tử ra khỏi stack và thêm vào danh sách biểu thức hậu tố
            elif bt[i] == ')':
                while toan_tu_stack and toan_tu_stack[-1] != '(':
                    hau_to.append(toan_tu_stack.pop())
                toan_tu_stack.pop()  # Xóa dấu '('

            # Nếu là toán tử, xử lý độ ưu tiên và đẩy vào stack toán tử
            elif la_toan_tu(bt[i]):
                while toan_tu_stack and do_uu_tien(bt[i]) <= do_uu_tien(toan_tu_stack[-1]):
                    hau_to.append(toan_tu_stack.pop())
                toan_tu_stack.append(bt[i])

            i += 1

        # Pop các toán tử còn lại ra khỏi stack và thêm vào danh sách biểu thức hậu tố
        while toan_tu_stack:
            hau_to.append(toan_tu_stack.pop())

        return ' '.join(hau_to)


# Sử dụng phương thức HauTo để chuyển đổi biểu thức
bt = "2 + 3 * 5"
solution = Solution()
print("Biểu thức hậu tố tương ứng là:", solution.HauTo(bt))

