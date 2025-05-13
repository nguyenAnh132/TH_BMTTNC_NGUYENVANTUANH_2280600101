row = int(input("Nhập vào số dòng: "))
col = int(input("Nhập vào số cột: "))
matrix = [[0 for col in range(col)] for row in range(row)]
for r in range(row):
    for c in range(col):
        matrix[r][c] = r* c
print(matrix)