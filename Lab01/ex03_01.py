def tinhTongSoChan(danhSach) : 
    tong = 0
    for so in danhSach :
        if so % 2 == 0:
            tong += so
    return tong

danhSachInput = input("Nhập vào danh sách các số (cách nhau bởi dấu phẩy): ")
danhSach = list(map(int, danhSachInput.split(',')))
tongChan = tinhTongSoChan(danhSach)
print("Tổng các số chẵn trong danh sách: ", tongChan)