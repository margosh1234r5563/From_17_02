number = int(input('Введите число: '))
while int(number ** 0.5) * int(number ** 0.5) != number:
    number = int(input('Введите число: '))
else:
    print('Ваше число полный квадрат')
