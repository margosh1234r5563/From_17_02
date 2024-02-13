# Task 12
total_cost = int(input('Введите общую стоимость часов: '))
amount_silver_clock = 96
amount_golden_clock = amount_silver_clock / 16
price_silver_clock = 48
cost_silver = amount_silver_clock * price_silver_clock
cost_golden_clock = total_cost - cost_silver
price_golden_clock = cost_golden_clock / amount_golden_clock
if price_golden_clock > 0:
    print(price_golden_clock)
else:
    print('Цена золотых часов не может быть отрицательной')