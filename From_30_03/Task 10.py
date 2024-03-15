import matplotlib.pyplot as plt

x1, y1, x2, y2, a1, b1, a2, b2 = map(int, input().split())

if a2 < x1 or x2 < a1 or b2 < y1 or y2 < b1:
    print("Прямоугольники лежат вне друг друга, не касаясь")
elif ((a1 == x2 or a2 == x1) and (b1 <= y2 and b2 >= y1)) or ((b1 == y2 or b2 == y1) and (a1 <= x2 and a2 >= x1)):
    print("Прямоугольники имеют касание")
elif a1 <= x2 and x1 <= a2 and b1 <= y2 and y1 <= b2:
    print("Прямоугольники имеют пересечение")
elif x1 <= a1 and x2 >= a2 and y1 <= b1 and y2 >= b2:
    print("Один прямоугольник лежит внутри другого, не касаясь")

fig, ax = plt.subplots()

a = abs(x1 - x2)
b = abs(y1 - y2)
c = abs(a1 - a2)
d = abs(b1 - b2)

frst_x = x2 - b
frst_y = y1 - a
scnd_x = a2 - d
scnd_y = b1 - c

plt.xlim(min(x2, a2) - 80, max(x2, a2) + 80)
plt.ylim(min(y1, b1) - 80, max(y1, b1) + 80)
rectangle1 = plt.Rectangle((frst_x, frst_y), a, b, color='red', fill=False)
rectangle2 = plt.Rectangle((scnd_x, scnd_y), c, d, color='k', fill=False)
plt.grid(linestyle='dotted')

ax.add_artist(rectangle1)
ax.add_artist(rectangle2)
plt.show()
