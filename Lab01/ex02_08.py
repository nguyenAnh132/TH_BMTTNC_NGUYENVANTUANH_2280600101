def chiaHetCho5(soNhiPhan):
    soThapPhan = int(soNhiPhan, 2)
    if soThapPhan % 5 == 0 :
        return True
    else :
        return False
    
chuoiSoNhiPhan = input("Nhập chuỗi số nhị phân (phân tách nhau bởi dấu phẩy): ")
danhSachSoNhiPhan = chuoiSoNhiPhan.split(',')
soChiaHetCho5 = [so for so in danhSachSoNhiPhan if chiaHetCho5(so)]
if len(soChiaHetCho5) > 0 :
    print("Các số nhị phân chia hết cho 5 là: ", ','.join(soChiaHetCho5))
else :
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập")