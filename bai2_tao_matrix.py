while True:
    try:
        n = int(input('Mời nhập số hàng: '))
        m = int(input('Mời nhập số cột: '))
    except ValueError as e:
        print('Invalid, Restart!')
        continue
    if m > 0 and n > 0:
        print(f'Matrx bao gồm {n} hàng {m} cột ')
        break

import random
lst = []
for i in range(n):
    lst.append([]) #Tạo ra từng list(từng hàng)
    for j in range(m):
        lst[i].append(random.randrange(0,9)) #i tại đây là list thứ 1 (hàng 1)

print(lst)