n = input()
first_letter = n[0]
first_number = int(n[1])
second_letter = n[3]
second_number = int(n[4])
if ord(first_letter) > ord('h') or first_number > 8 or ord(second_letter) > ord('h') or second_number > 8:
    print('ход невозможен')
dx = abs(ord(first_letter) - ord(second_letter))
dy = abs(first_number - second_number)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('верно')
else:
    print('ошибка')
