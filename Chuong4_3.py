class Solution:
    def GiaTri(self, bt):
        # Hàm để thực hiện một phép toán
        def tinh(toan, operand1, operand2):
            if toan == '+':
                return operand1 + operand2
            elif toan == '-':
                return operand1 - operand2
            elif toan == '*':
                return operand1 * operand2
            elif toan == '/':
                return operand1 / operand2

        # Hàm để kiểm tra xem một ký tự có phải là toán tử hay không
        def la_toan_tu(char):
            return char in '+-*/'

        toan_hang_stack = []  # Stack lưu trữ các toán hạng
        toan_tu_stack = []  # Stack lưu trữ các toán tử

        i = 0
        while i < len(bt):
            # Bỏ qua khoảng trắng
            if bt[i] == ' ':
                i += 1
                continue

            # Nếu là dấu mở ngoặc, đẩy vào stack toán tử
            elif bt[i] == '(':
                toan_tu_stack.append(bt[i])

            # Nếu là toán tử, đẩy vào stack toán tử và thực hiện các phép toán có ưu tiên cao hơn
            elif la_toan_tu(bt[i]):
                while toan_tu_stack and toan_tu_stack[-1] != '(' and (
                        (bt[i] == '*' or bt[i] == '/') and (toan_tu_stack[-1] == '+' or toan_tu_stack[-1] == '-')):
                    toan_hang2 = toan_hang_stack.pop()
                    toan_hang1 = toan_hang_stack.pop()
                    toan_tu = toan_tu_stack.pop()
                    toan_hang_stack.append(tinh(toan_tu, toan_hang1, toan_hang2))
                toan_tu_stack.append(bt[i])

            # Nếu là dấu đóng ngoặc, thực hiện các phép toán trong ngoặc
            elif bt[i] == ')':
                while toan_tu_stack and toan_tu_stack[-1] != '(':
                    toan_hang2 = toan_hang_stack.pop()
                    toan_hang1 = toan_hang_stack.pop()
                    toan_tu = toan_tu_stack.pop()
                    toan_hang_stack.append(tinh(toan_tu, toan_hang1, toan_hang2))
                toan_tu_stack.pop()  # Xóa dấu '('

            # Nếu là toán hạng, đẩy vào stack toán hạng
            else:
                toan_hang = ''
                while i < len(bt) and bt[i].isdigit():
                    toan_hang += bt[i]
                    i += 1
                toan_hang_stack.append(int(toan_hang))
                continue

            i += 1

        # Thực hiện các phép toán còn lại
        while toan_tu_stack:
            toan_hang2 = toan_hang_stack.pop()
            toan_hang1 = toan_hang_stack.pop()
            toan_tu = toan_tu_stack.pop()
            toan_hang_stack.append(tinh(toan_tu, toan_hang1, toan_hang2))

        # Kết quả cuối cùng sẽ ở trên đỉnh stack toán hạng
        return toan_hang_stack[-1]

# Sử dụng phương thức GiaTri để tính giá trị của biểu thức
bt = "(3 + 4) * 2 / ( 3 - 1 )"
solution = Solution()
print("Giá trị của biểu thức là:", solution.GiaTri(bt))
