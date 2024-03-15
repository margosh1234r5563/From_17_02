name = input()
letter = name[0]
number = int(name[1])
if ord(letter) > ord('h') or number > 8:
    print('это невозможно')
elif ord(letter) % 2 == 0:
    if number % 2 == 1:
        print('белый')
    else:
        print('черный')
elif ord(letter) % 2 == 1:
    if number % 2 == 1:
        print('черный')
    else:
        print('белый')
