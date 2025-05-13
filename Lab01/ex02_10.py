def daoNguocChuoi(chuoi) :
    return chuoi[::-1]
chuoi = input("Nhập chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược là: ", daoNguocChuoi(chuoi))