def demSoLanXuatHien(danhSach) :
    count_dict = {}
    for item in danhSach :
        if item in count_dict :
            count_dict[item] += 1
        else :
            count_dict[item] = 1
    return count_dict

inputString = input("Nhập vào danh sách các từ, cách nhau bằng dấu cách: ")
wordList = inputString.split()

soLanXuanHien = demSoLanXuatHien(wordList)
print("Số lần xuất hiện của các phần tử: ", soLanXuanHien)
