def truyCapPhanTu(tupleData) :
    first_element = tupleData[0]
    last_element = tupleData[-1]
    return first_element, last_element

inputTuple = eval(input("Nhập tuple, ví dụ (1,2,3): "))
first, last = truyCapPhanTu(inputTuple)

print("Phần tử đầu tiên: ", first)
print("Phần tử cuối cùng: ", last)