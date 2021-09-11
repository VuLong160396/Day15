
#Bai 2
list_name = []
list_gender = []
list_home = []
list_theory = []
list_practice = []
list_student = [list_name,list_gender,list_home,list_theory,list_practice]
theory = 0
practice = 0

#Tiêu đề
print('|','*'*80,'|')
print('{0:^20}|{1:^10}|{2:^20}|{3:^10}|{4:^10}'.format('Name','Gender','Hometown','Theory','Practice'))
print('|','*'*80,'|')
#Nhập thông tin
while True:
    name = input('Name: ')
    if name in list_name:
        print('Name is exists, please try again!')
        continue
    else:
        list_name.append(name)

        gender = input('Gender: ')
        list_gender.append(gender)

        home = input('Home: ')
        list_home.append(home)

        while True:
            try:
                theory = int(input('Theory(0-100): '))
            except ValueError:
                print('Invalid! Theory in (0-100)')
                continue
            if 0 <= theory <= 100:
                list_theory.append(theory)
                break
            else:
                print(f'{theory} invalid!')
                continue

        while True:
            try:
                practice = int(input('Practice(0-100): '))
            except ValueError:
                print('Invalid! Practice in (0-100)')
                continue
            if 0 <= practice <= 100:
                list_practice.append(practice)
                break
            else:
                print('Invalid! Practice in (0-100)')
                continue

        cont = input('Continue?(n): ')

        if cont == 'n':
            break
        else:
            continue

#Hiển thị tiêu đề
print('|','*'*80,'|')
print('{0:^20}|{1:^10}|{2:^20}|{3:^10}|{4:^10}'.format('Name','Gender','Hometown','Theory','Practice'))
print('|','*'*80,'|')

#Hiển thị thông tin sinh viên
for i in range(len(list_name)):
    print(f'{list_name[i]:^20}|{list_gender[i]:^10}|{list_home[i]:^20}|{list_theory[i]:^10}|{list_practice[i]:^10}')

#Trang trí
print('|','*'*80,'|')

del_sv = input('Do you want to delete student in lits(y/n): ')
if del_sv == 'y':
    sv_name = input('Enter name: ')
    if sv_name in list_name:
        del_pos = list_name.index(sv_name)
        #tiêu đề    
        print('|','*'*80,'|')
        print('{0:^20}|{1:^10}|{2:^20}|{3:^10}|{4:^10}'.format('Name','Gender','Hometown','Theory','Practice'))
        print('|','*'*80,'|')

        #Hiển thị thông tin sinh viên
        for i in range(len(list_name)):
            if i == del_pos:
                pass
            else:
                print(f'{list_name[i]:^20}|{list_gender[i]:^10}|{list_home[i]:^20}|{list_theory[i]:^10}|{list_practice[i]:^10}')

        #tiêu đề
        print('|','*'*80,'|')
    else:
        print(f'{sv_name} not in list name' )
else:
    exit()



