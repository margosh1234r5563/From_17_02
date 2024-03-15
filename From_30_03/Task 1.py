import math

s = math.pi * 6.5
a, b = map(int, input().split('x'))
if a * b < s:
    print('да')
else:
    print('нет')
