n = int(input())
count = 0
for i in range(2, n):
    for m in range(2, i):
        if i % m == 0:
            count += 1
    if count == 0:
        print(i)
    count = 0
