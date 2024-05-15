class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

class CayNhiPhan:
    def __init__(self):
        self.root = None

    def SoNut(self, node):
        if node is None:
            return 0
        else:
            return self.SoNut(node.left) + 1 + self.SoNut(node.right)

    def TongSoNut(self):
        return self.SoNut(self.root)

# Sử dụng đoạn mã
# Tạo cây nhị phân
tree = CayNhiPhan()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# In ra số nút của cây
print("Số nút của cây nhị phân là:", tree.TongSoNut())
