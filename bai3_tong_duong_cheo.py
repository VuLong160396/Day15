from random import randrange
#Tạo ma trận ngẫu nhiên từ kích thước được nhập từ bàn phím
n = int(input('Nhập số kích thước ma trận(hàng = cột):'))
lst = []
for i in range(n):
    lst.append([])
    for j in range(n) :
        lst[i].append(randrange(0,9))
print('Ma trận được tạo ra:',lst)

#Hàm tính tổng đường chéo chính của ma trận
def sum_diagonal(list1):
    # print(len(list1))
    sum_diag = 0
    for i in range(len(list1)):
        sum_diag += list1[i][i]
    return(sum_diag)

print('Tổng đường chéo chính của ma trận: ',sum_diagonal(lst))