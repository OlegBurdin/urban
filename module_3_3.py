def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

#print_params(b = 25, c = 'Lol', d = True) ошибка, нельзя вводить больше параметров, чем указано в функции
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [False, 'Well Well Well', 1]
values_dict = {1 : 1, 2 : 'строка', 3 : [True, 'pep8']}

print_params(*values_list)
print_params(*values_dict)

values_list_2 = [213, 'айналайын']
print_params(*values_list_2, 42) #работает
