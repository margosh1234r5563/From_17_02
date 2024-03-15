n = int(input())
if n % 10 == 1 and n != 11:
    print(n, 'попугай')
elif (n % 10 >= 2 and n % 10 <= 4) and (n != 11 and n != 12 and n != 13 and n != 14):
    print(n, 'попугая')
elif (n % 10 == 0) or (n % 10 >= 5 and n % 10 <= 9) or n == 100 or (n >= 11 or n <= 14):
    print(n, 'попугаев')
