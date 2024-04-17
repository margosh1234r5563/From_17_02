n = int(input())
for i in range(n, 1, -1):
    if n % i == 0 and n // i >= 2:
        print(n // i)
        break
