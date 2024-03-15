a, b = map(int, input().split('x'))
s = a * b
c, d, e = map(int, input().split('x'))
if c * d < s or c * e < s or d * e < s:
    print('да')
else:
    print('нет')
