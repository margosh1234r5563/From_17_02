n, m = map(int, input().split('x'))
g = int(input())
if g > m * n or n == 0 or m == 0 or g == 0:
    print('неосуществимо')
elif n == 1 or m == 1:
    print('успешно')
elif m * n % 2 == 0 and g % 2 == 0:
    print('успешно')
elif m * n % 2 == 1 and g % 2 == 1:
    print('успешно')
else:
    print('неосуществимо')
