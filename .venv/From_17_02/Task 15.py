# Task 15
cm = float(input('Введите расстояние в сантиметрах: '))
d = cm / 2.54
f = cm / (2.54 * 12)
yard = cm / (2.54 * 12 * 3)
miles = cm / (2.54 * 12 * 3 * 1760)
print(yard, 'ярдов')
print(miles, 'мили')
print(f, 'футов')
print(d, 'дюймов')
