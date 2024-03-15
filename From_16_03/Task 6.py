day_1 = int(input())
day_2 = int(input())
day_3 = int(input())
amount = 1
if day_1 == day_2:
    amount += 1
    if day_1 == day_3:
        amount += 1
elif day_1 == day_3:
    amount += 1
    if day_1 == day_2:
        amount += 1
elif day_2 == day_3:
    amount += 1
    if day_2 == day_1:
        amount += 1
print(amount)
