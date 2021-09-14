tupl = (
    (1,2,3,4), 
    (3,5,2,1), 
    (2,2,3,1)
)
# from random import randrange
# #Tạo tuple ngẫu nhiên:
# while True:
#     try:
#         m = int(input('Nhập số hàng: '))
#         n = int(input('Nhập số cột: '))
#     except ValueError:
#         print('Không hợp lệ vui lòng nhập lại!')
#         continue
#     if m > 0 and n > 0:
#         break
# tupl =tuple(i for i in range(m))
# print(tupl)
# # for i in range(m):
# #     tupl((),)
# #     for j in range(n):
# #         tupl[i].append(randrange(0,9))


def sum_row_elements(tuple1):
    lst = []
    for j in range(len(tuple1[0])): #Hàm chạy từ phần tử 1 đến phần tử 4 của list nhỏ
        lst.append([])
        for i in range(len(tuple1)): #Hàm chạy từ list nhỏ 1 đến list nhỏ 3 của tuple1
            lst[j].append(tuple1[i][j])
    # print(lst) #Gom các phần tử cùng vị trí vào cùng list

    final_lst = []
    for i in range(len(lst)):
        final_lst.append(sum(lst[i]))
    return final_lst

print(sum_row_elements(tupl))
