def daoNguoc(danhSach) : 
    return danhSach[::-1]

danhSachInput = input("Nhập danh sách các số (cách nhau bởi dấu phẩy): ")
danhSach = list(map(int, danhSachInput.split(',')))
danhSachDaoNguoc = daoNguoc(danhSach)
print("Danh sách sau khi đảo ngược: ", danhSachDaoNguoc)