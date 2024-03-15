import math

n, k, m = map(int, input().split())
amount_ride = n * 2
amount_start = math.ceil(n * 2 / k)
print(amount_start * m)
