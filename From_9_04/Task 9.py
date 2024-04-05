n, k, r = map(int, input().split())
count = 1
while n < r:
    n = n + (k / 100) * n
    count += 1
print(count)
