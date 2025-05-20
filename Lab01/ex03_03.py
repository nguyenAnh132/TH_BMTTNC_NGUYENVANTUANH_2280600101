def taoTuple(danhSach) :
    return tuple(danhSach)

danhSachInput = input("Nhập danh sách các số (cách nhau bởi dấu phẩy): ")
danhSach = list(map(int, danhSachInput.split(',')))

myTuple = taoTuple(danhSach)
print("List: ", danhSach)
print("Tuple từ List: ", myTuple)