number_0 = float(input())
count = 0

while True:
    number = float(input())
    if number == 0:
        break
    if number < number_0:
        count += 1
    number_0 = number
print(count)
