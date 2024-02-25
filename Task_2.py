a = int(input())
if a >= 1 and a <= 86400:
    hours = a // 3600
    munutes = (a - hours * 3600) // 60
    second = a - hours * 3600 - munutes * 60
    print(hours, 'часов', munutes, 'минут', second, 'секунд')
else:
    print('Число вне заданного диапозона')
