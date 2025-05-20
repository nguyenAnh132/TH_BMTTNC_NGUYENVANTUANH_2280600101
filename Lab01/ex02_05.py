GIO_TIEU_CHUAN = 44
soGioLam = float(input("Nhập số giờ làm mỗi tuần: "))
thuLao = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
gioVuotChuan = max(0, soGioLam - GIO_TIEU_CHUAN)
thucLinh = GIO_TIEU_CHUAN * thuLao + gioVuotChuan * thuLao * 1.5
print(f"Số tiền thực lĩnh của nhân viên: ", thucLinh)