print('Как зовут главных героев компьютерной игры Minecraft?')
name_first = input('Имя первого героя: ')
name_second = input('Имя второго героя: ')
if (
        name_first == 'Алекс' or name_first == 'Стив' or name_second == 'Алекс' or name_second == 'Стив') and name_first != name_second:
    print('Верно')
else:
    print('Неверно')
