cost = float(input())
cost = int(cost)
cost = str(cost)
if len(cost) != 7:
    print('К сожаленю цена в биткоинах 7 значное число')
else:
    cost = float(cost)
    cost = cost // 100 % 100 % 10
    print(int(cost))
