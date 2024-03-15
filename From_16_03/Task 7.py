n, k, m = map(int, input().split())
'''
if m > k and m <= n and k <= n:
   if 
   print(m - k - 1)
'''
if n > k and m <= n:
    if k < m:
        print(m - k - 1)
    else:
        print(n - (abs(m - k) + 1))
