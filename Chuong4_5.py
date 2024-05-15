class HanoiTower:
    def __init__(self, n):
        self.n = n  # Số tầng của tháp
        self.source = list(range(n, 0, -1))  # Tháp nguồn, có n tầng
        self.target = []  # Tháp đích, ban đầu rỗng
        self.auxiliary = []  # Tháp trung gian, ban đầu rỗng

    def move(self, source, target, disk):
        target.append(disk)
        source.pop()
        print("Di chuyển tầng", disk, "từ tháp", source, "đến tháp", target)

    def solve(self):
        print("Bắt đầu di chuyển tháp:")
        self._move_tower(self.n, self.source, self.target, self.auxiliary)

    def _move_tower(self, n, source, target, auxiliary):
        if n == 1:
            self.move(source, target, source[-1])
        else:
            self._move_tower(n - 1, source, auxiliary, target)
            self.move(source, target, source[-1])
            self._move_tower(n - 1, auxiliary, target, source)


# Sử dụng lớp HanoiTower để di chuyển tháp và in ra các bước di chuyển
n = 3  # Số tầng của tháp
tower = HanoiTower(n)
tower.solve()


