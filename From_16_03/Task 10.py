a = int(input())
a1 = a // 1000
a2 = a // 100 % 10
a3 = a // 10 % 10 % 10
a4 = a % 10 % 10 % 10

if a // 10000 == 0 and a // 1000 > 0:
    if (a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4) or (
            a1 == 1 and a2 == 9 and a3 >= 0 and a4 >= 0) or (a1 == 2 and a2 == 0 and a3 <= 5 and a4 >= 0):
        print('ERROR')
    else:
        print('OK')
else:
    print('ERROR')
