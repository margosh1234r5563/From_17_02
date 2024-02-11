#Task 12
print('Введите общую стоимость часов')
total_cost=int(input())
amount_silver_clock=96
amount_golden_clock=amount_silver_clock / 16
price_silver_clock=48
cost_silver=amount_silver_clock * price_silver_clock
cost_golden_clock=total_cost - cost_silver
price_golden_clock=cost_golden_clock / amount_golden_clock
print(price_golden_clock)