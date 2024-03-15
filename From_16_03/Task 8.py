n = int(input())
sickles = n // 29
amount_galeons = n // 493
amount_sickles = sickles - amount_galeons * 17
amount_knuts = n - amount_sickles * 29 - amount_galeons * 493
if amount_galeons != 0:
    print(f'{amount_galeons} галлеонов')
if amount_sickles != 0:
    print(f'{amount_sickles}  сиклей')
if amount_knuts != 0:
    print(f'{amount_knuts} кнатов')
