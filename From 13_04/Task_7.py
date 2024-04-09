a = input('Введите число: ')
while a.isdigit() != True:
    if a.isdigit() == 1:
        break
    else:
        a = input('Ошибка. Попробуйте еще раз. Введите число: ')
print('Введено целое число:', a)
