def kiemTraNT(so) :
    if so <= 1 :
        return False
    for i in range (2, int(so**0.5) + 1) :
        if so % i == 0 : 
            return False
    return True

so = int(input("Nhập vào số cần kiểm tra: "))
if kiemTraNT(so) :
    print(so, " là số nguyên tố")
else :
    print(so, " không phải là số nguyên tố")