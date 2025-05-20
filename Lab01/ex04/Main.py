from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (True):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("******************MENU******************")
    print("** 1. Them sinh vien.                  **")
    print("** 2. Cap nhat thong tin sinh vien boi ID.**")
    print("** 3. Xoa sinh vien boi ID.             **")
    print("** 4. Tim kiem sinh vien theo ten.      **")
    print("** 5. Sap xep sinh vien theo diem trung binh.**")
    print("** 6. Sap xep sinh vien theo ten chuyen nganh.**")
    print("** 7. Hien thi danh sach sinh vien.     **")
    print("** 0. Thoat.                           **")
    print("*****************************************")

    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien boi ID.")
            idCanUpdate = int(input("Nhap ID: "))
            qlsv.updateSinhVien(idCanUpdate)
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien.")
            ID = int(input("Nhap ID: "))
            if(qlsv.deleteById(ID)):
                print("Sinh vien co id = ", ID," da bi xoa.")
            else:
                print("Khong tim thay sinh vien co id = ", ID," de bi xoa.")
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 4):
        print("\n4. Tim kiem sinh vien theo ten.")
        if (qlsv.soLuongSinhVien() > 0):
            name = input("Nhap ten de tim kiem: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 5):
        print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
        if (qlsv.soLuongSinhVien() > 0):
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 6):
        print("\n6. Sap xep sinh vien theo ten.")
        if (qlsv.soLuongSinhVien() > 0):
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 7):
        print("\n7. Hien thi danh sach sinh vien.")
        if (qlsv.soLuongSinhVien() > 0):
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 0):
        print("\nBan da chon thoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("Hay chon chuc nang trong hop menu.")