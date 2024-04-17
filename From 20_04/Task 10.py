n = int(input())
d = [1] + [0] * n
for i in range(n):
    for j in range(n, i, -1):
        d[j] += d[j - i - 1]
print(d[n])
