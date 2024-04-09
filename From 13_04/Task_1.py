result = int(input())
max_result = result
while result != -1:
    result_1 = int(input())
    if result_1 == -1:
        break
    else:
        if result_1 >= result:
            max_result = result_1
    result = result_1
print(max_result)
