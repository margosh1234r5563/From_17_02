num = int(input())
count = 0
for i in range(1, num + 1):
    for s in range(1, num + 1):
        if i ** 2 + s ** 2 == num:
            count += 1
print(count // 2)
