def xoaPhanTu(dictionary, key) :
    if key in dictionary : 
        del dictionary[key]
        return key
    else :
        return False
    
my_dict = {'a' : 1, 'b': 2, 'c' : 3, 'd' : 4}
keyToDelete = 'b'
result = xoaPhanTu(my_dict, keyToDelete)
if result :
    print("Phần tử đã được xoá từ Dictionary: ", my_dict)
else :
    print("Không tìm thấy phần tử cần xoá trong Dictionary.")