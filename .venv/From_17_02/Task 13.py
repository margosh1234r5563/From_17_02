#Task 13
import math as m
print('Введите радиус "слепой зоны"')
r_small_zone=int(input())
print('Введите радиус "дальности приема"')
r_big_zone=int(input())
s_small_zone=m.pi * r_small_zone ** 2
s_big_sone=m.pi * r_big_zone ** 2
s_cover=s_big_sone-s_small_zone
print('Площадь покрываемой территории', s_cover)
