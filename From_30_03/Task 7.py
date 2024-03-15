k = int(input())
count = 0
for i in range(1, k // 5):
    if (k - i * 5) % 7 == 0:
        count += 1
if count >= 1:
    print('да')
else:
    print('нет')
