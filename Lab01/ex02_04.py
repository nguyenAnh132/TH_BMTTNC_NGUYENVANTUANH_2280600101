START = 2000
END = 3200 + 1
list = []
for i in range(START, END):
    if (i % 7 == 0) and (i % 5 != 0):
        list.append(str(i))
print(", ".join(list))