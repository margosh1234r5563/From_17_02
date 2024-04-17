n = int(input())
count = 0
for i in range(1, n + 1):
    for m in range(1, n + 1):
        count += i + m
print(count)
