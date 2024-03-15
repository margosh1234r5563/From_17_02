first_high, second_high, third_high = map(int, input().split())
if first_high >= second_high:
    if second_high >= third_high:
        print(first_high, second_high, third_high)
    else:
        if first_high >= third_high:
            print(first_high, third_high, second_high)
        else:
            print(third_high, first_high, second_high)
if first_high <= second_high:
    if second_high >= third_high:
        if third_high >= first_high:
            print(second_high, third_high, first_high)
        else:
            print(second_high, first_high, third_high)
    else:
        print(third_high, second_high, first_high)
