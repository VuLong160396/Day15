#hàm check nguyên tố
def check_nt(lst1):
    lst_nt = []
    for i in lst1:
        count = 0
        for j in range(2,(i//2+1)):
            if i % j ==0:
                count += 1
        if count == 0:
            lst_nt.append(i)
    return lst_nt

#Nhập số lượng và phần tử
while True:
    try:
        n = int(input('Nhập số lượng các phần tử (n>0): '))
    except ValueError as e:
        print('Invalid')
    if n > 0:
        print(f'List gồm {n} phần tử')
        break
    else:
        print('Invalid')
        continue

list1 = []
for i in range(n):
    list1.append(int(input(f'Nhập phần tử thứ {i+1}: ')))

# list1 = [1,2,3,4,5]
if __name__ == '__main__':
    a = check_nt(list1)
    print('Các số nguyên tố trong list là: ',list(set(a)))
    