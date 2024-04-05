number = int(input())
count = 1
while count < number:
    count *= 2
    if count <= number:
        print(count)
