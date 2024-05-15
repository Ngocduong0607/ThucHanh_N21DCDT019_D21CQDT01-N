import pickle

class Node:
    def __init__(self, tu, nghia=None):
        self.tu = tu
        self.nghia = nghia if nghia else []
        self.trai = None
        self.phai = None

class TuDienBST:
    def __init__(self):
        self.goc = None

    def them(self, tu, loai_tu, nghia, vi_du=None):
        if not self.goc:
            self.goc = Node(tu)
            self.goc.nghia.append((loai_tu, nghia, vi_du))
        else:
            self._them_de_quy(self.goc, tu, loai_tu, nghia, vi_du)

    def _them_de_quy(self, nut, tu, loai_tu, nghia, vi_du):
        if tu == nut.tu:
            nut.nghia.append((loai_tu, nghia, vi_du))
        elif tu < nut.tu:
            if nut.trai is None:
                nut.trai = Node(tu)
                nut.trai.nghia.append((loai_tu, nghia, vi_du))
            else:
                self._them_de_quy(nut.trai, tu, loai_tu, nghia, vi_du)
        else:
            if nut.phai is None:
                nut.phai = Node(tu)
                nut.phai.nghia.append((loai_tu, nghia, vi_du))
            else:
                self._them_de_quy(nut.phai, tu, loai_tu, nghia, vi_du)

    def tim_kiem(self, tu):
        return self._tim_kiem_de_quy(self.goc, tu)

    def _tim_kiem_de_quy(self, nut, tu):
        if nut is None:
            return None
        if nut.tu == tu:
            return nut.nghia
        elif tu < nut.tu:
            return self._tim_kiem_de_quy(nut.trai, tu)
        else:
            return self._tim_kiem_de_quy(nut.phai, tu)

    def xoa(self, tu):
        self.goc = self._xoa_de_quy(self.goc, tu)

    def _xoa_de_quy(self, nut, tu):
        if nut is None:
            return None
        if tu == nut.tu:
            if nut.trai is None:
                return nut.phai
            elif nut.phai is None:
                return nut.trai
            else:
                nut_nho_nhat = self._tim_min(nut.phai)
                nut.tu = nut_nho_nhat.tu
                nut.nghia = nut_nho_nhat.nghia
                nut.phai = self._xoa_de_quy(nut.phai, nut_nho_nhat.tu)
        elif tu < nut.tu:
            nut.trai = self._xoa_de_quy(nut.trai, tu)
        else:
            nut.phai = self._xoa_de_quy(nut.phai, tu)
        return nut

    def _tim_min(self, nut):
        hien_tai = nut
        while hien_tai.trai:
            hien_tai = hien_tai.trai
        return hien_tai

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.goc, f)

    def load_from_file(self, filename):
        with open(filename, 'rb') as f:
            self.goc = pickle.load(f)

def hien_thi_menu():
    print("Trình đơn Từ điển:")
    print("1. Thêm từ mới")
    print("2. Xóa một từ")
    print("3. Tìm kiếm nghĩa của từ")
    print("4. Lưu từ điển vào tập tin")
    print("5. Nạp từ điển từ tập tin")
    print("6. Thoát")

def chuong_trinh_chinh():
    tu_dien = TuDienBST()
    ma_sinh_vien = "mãsinhviên"  # Thay thế bằng mã sinh viên của bạn

    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == "1":
            tu = input("Nhập từ: ")
            loai_tu = input("Nhập loại từ: ")
            nghia = input("Nhập nghĩa: ")
            vi_du = input("Nhập ví dụ (nếu có): ")
            tu_dien.them(tu, loai_tu, nghia, vi_du)
            print("Từ được thêm vào từ điển.")
        elif lua_chon == "2":
            tu = input("Nhập từ cần xóa: ")
            tu_dien.xoa(tu)
            print("Từ được xóa khỏi từ điển.")
        elif lua_chon == "3":
            tu = input("Nhập từ cần tìm kiếm: ")
            nghia = tu_dien.tim_kiem(tu)
            if nghia:
                print("Nghĩa:")
                for nghia_tu in nghia:
                    print("Loại từ:", nghia_tu[0])
                    print("Nghĩa:", nghia_tu[1])
                    if nghia_tu[2]:
                        print("Ví dụ:", nghia_tu[2])
            else:
                print("Từ không được tìm thấy trong từ điển.")
        elif lua_chon == "4":
            ten_tap_tin = f"{ma_sinh_vien}_BST.pkl"
            tu_dien.save_to_file(ten_tap_tin)
            print(f"Từ điển được lưu vào tập tin {ten_tap_tin}.")
        elif lua_chon == "5":
            ten_tap_tin = f"{ma_sinh_vien}_BST.pkl"
            tu_dien.load_from_file(ten_tap_tin)
            print(f"Từ điển được nạp từ tập tin {ten_tap_tin}.")
        elif lua_chon == "6":
            print("Đang thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    chuong_trinh_chinh()
