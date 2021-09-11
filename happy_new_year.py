#Bai 1:
my_list = ['Nguyen',"Tra",'Quoc','Chung']
print(f'List name: {my_list}')

while True:
    name = input('Hãy điền tên người trong list muốn chúc: ')
    if name in my_list:
        print('*'*10,f'Happy new year, {name}','*'*10)
        break
    elif name == 'all':
        for name in my_list:
            print('*'*10,f'Happy new year, {name}','*'*10, end='\n'*2)
        break
    else:
        print('Sorry, Please again!')
