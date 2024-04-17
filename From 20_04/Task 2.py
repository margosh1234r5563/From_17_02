import math

num = int(input())
if num > 2:
    while num > 2:
        num = math.sqrt(num)
        print(round(num, 3))
