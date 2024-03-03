a, b, c = map(str, input().split())
a = int(a)
c = int(c)
if a > c:
    print('Первая команда выиграла')
elif c < a:
    print('Вторая команда выиграла')
else:
    print('0')
