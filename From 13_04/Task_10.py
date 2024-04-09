n = int(input())
sum_devided = 0
for i in range(2, n + 1):
    for n in range(1, i):
        if i % n == 0:
            sum_devided += n
    if sum_devided == i:
        print(i)
    sum_devided = 0
