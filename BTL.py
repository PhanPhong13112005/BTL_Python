import json

class DiemThi:
    def __init__(self, ma_hs, ten, ngay_sinh, gioi_tinh, mon_hoc, diem):
        self.ma_hs = ma_hs
        self.ten = ten
        self.ngay_sinh = ngay_sinh
        self.gioi_tinh = gioi_tinh
        self.mon_hoc = mon_hoc
        self.diem = diem

    def hien_thi_thong_tin(self):
        print(
            f"Mã HS: {self.ma_hs}, Tên: {self.ten}, Ngày Sinh: {self.ngay_sinh}, Giới Tính: {self.gioi_tinh}, "
            f"Môn Học: {self.mon_hoc}, Điểm: {self.diem}"
        )

    def to_dict(self):
        return {
            "ma_hs": self.ma_hs,
            "ten": self.ten,
            "ngay_sinh": self.ngay_sinh,
            "gioi_tinh": self.gioi_tinh,
            "mon_hoc": self.mon_hoc,
            "diem": self.diem
        }

class QuanLyDiemThi:
    def __init__(self):
        self.danh_sach_diem = []

    def them_diem_thi(self, diem_thi):
        self.danh_sach_diem.append(diem_thi)

    def xoa_diem_thi(self, ma_hs, mon_hoc):
        self.danh_sach_diem = [dt for dt in self.danh_sach_diem if not (dt.ma_hs == ma_hs and dt.mon_hoc == mon_hoc)]

    def sua_diem_thi(self, ma_hs, mon_hoc, diem_moi=None):
        for dt in self.danh_sach_diem:
            if dt.ma_hs == ma_hs and dt.mon_hoc == mon_hoc:
                if diem_moi is not None:
                    dt.diem = diem_moi

    def hien_thi_danh_sach_diem(self):
        for dt in self.danh_sach_diem:
            dt.hien_thi_thong_tin()

    def tinh_diem_trung_binh(self):
        if not self.danh_sach_diem:
            print("Chưa có dữ liệu.")
            return
        tong_diem = sum(dt.diem for dt in self.danh_sach_diem)
        so_hs = len(self.danh_sach_diem)
        diem_trung_binh = tong_diem / so_hs if so_hs > 0 else 0
        print(f"Điểm trung bình của tất cả học sinh: {diem_trung_binh:.2f}")

    def luu_du_lieu(self, file_name):
        with open(file_name, 'w') as file:
            json.dump([dt.to_dict() for dt in self.danh_sach_diem], file)

    def doc_du_lieu(self, file_name):
        try:
            with open(file_name, 'r') as file:
                danh_sach_diem = json.load(file)
                self.danh_sach_diem = [DiemThi(**dt) for dt in danh_sach_diem]
        except FileNotFoundError:
            print("File không tồn tại.")

def hien_thi_menu():
    print("======= MENU QUẢN LÝ ĐIỂM THI =======")
    print("1. Thêm điểm thi")
    print("2. Xóa điểm thi")
    print("3. Sửa điểm thi")
    print("4. Hiển thị danh sách điểm thi")
    print("5. Tính điểm trung bình")
    print("6. Lưu dữ liệu vào file")
    print("7. Đọc dữ liệu từ file")
    print("8. Thoát")
    print("======================================")

def main():
    ql_diem = QuanLyDiemThi()
    while True:
        hien_thi_menu()
        lua_chon = input("Mời bạn chọn: ")
        if lua_chon == '1':
            ma_hs = input("Nhập mã học sinh: ")
            ten = input("Nhập tên học sinh: ")
            ngay_sinh = input("Nhập ngày sinh: ")
            gioi_tinh = input("Nhập giới tính: ")
            mon_hoc = input("Nhập môn học: ")
            diem = float(input("Nhập điểm: "))
            diem_thi = DiemThi(ma_hs, ten, ngay_sinh, gioi_tinh, mon_hoc, diem)
            ql_diem.them_diem_thi(diem_thi)
        elif lua_chon == '2':
            ma_hs = input("Nhập mã học sinh cần xóa: ")
            mon_hoc = input("Nhập môn học: ")
            ql_diem.xoa_diem_thi(ma_hs, mon_hoc)
        elif lua_chon == '3':
            ma_hs = input("Nhập mã học sinh cần sửa: ")
            mon_hoc = input("Nhập môn học cần sửa điểm: ")
            diem_moi = float(input("Nhập điểm mới: "))
            ql_diem.sua_diem_thi(ma_hs, mon_hoc, diem_moi)
        elif lua_chon == '4':
            ql_diem.hien_thi_danh_sach_diem()
        elif lua_chon == '5':
            ql_diem.tinh_diem_trung_binh()
        elif lua_chon == '6':
            file_name = input("Nhập tên file để lưu: ")
            ql_diem.luu_du_lieu(file_name)
        elif lua_chon == '7':
            file_name = input("Nhập tên file để đọc: ")
            ql_diem.doc_du_lieu(file_name)
        elif lua_chon == '8':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
    
