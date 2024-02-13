# Task 13
import math as m
r_1_zone = int(input('Введите радиус первой зоны: '))
r_2_zone = int(input('Введите радиус второй зоны: '))
s_1_zone = m.pi * r_1_zone ** 2
s_2_zone = m.pi * r_2_zone ** 2
s_cover = s_2_zone - s_1_zone
print('Площадь покрываемой территории', abs(s_cover))
