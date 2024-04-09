amount = int(input())
amount_list = [amount]
while amount != 0:
    amount_1 = int(input())
    if amount_1 == 0:
        break
    else:
        amount_list.append(amount_1)
sum = 0
for i in range(0, len(amount_list)):
    sum += int(amount_list[i])
average_value = sum / (len(amount_list))
print(average_value)
