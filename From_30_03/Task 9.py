import math

import matplotlib.pyplot as plt

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

fig, ax = plt.subplots()

plt.xlim(-min(x1 + r1, x2 + r2) - 80, max(x1 + r1, x2 + r2) + 80)
plt.ylim(-min(y1 + r1, y2 + r2) - 80, max(y1 + r1, y2 + r2) + 80)
c1 = plt.Circle((x1, y1,), r1, color='k', fill=False)
c2 = plt.Circle((x2, y2), r2, color='k', fill=False)
plt.grid(linestyle='dotted')

ax.add_artist(c1)
ax.add_artist(c2)
ax.set_aspect('equal')

a = abs(r1 - r2)
print(a)

if r1 + r2 > abs(x1 - x2) and r1 + r2 > abs(y1 - y2):
    if abs(y1 - y2) == math.sqrt((r1 + r2) ** 2 - (x2 - x1) ** 2) or abs(x1 - x2) == math.sqrt(
            (r1 + r2) ** 2 - (y2 - y1) ** 2):
        plt.title('Окружности имеют внешнее касание', fontsize=8, color='red')
    elif abs(y1 - y2) > math.sqrt((r1 + r2) ** 2 - (x2 - x1) ** 2) or abs(x1 - x2) > math.sqrt(
            (r1 + r2) ** 2 - (y2 - y1) ** 2):
        plt.title('Окружности лежат одна вне другой, не касаясь', fontsize=8, color='red')
    elif math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) < r1 + r2:
        plt.title('Окружности пересекаются', fontsize=8, color='red')
    elif math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) > r1 + r2:
        plt.title('Окружности не пересекаются', fontsize=8, color='red')
elif r1 + r2 < abs(x1 - x2) or r1 + r2 < abs(y1 - y2):
    plt.title('Окружности не пересекаются', fontsize=8, color='red')
if abs(y1 - y2) == a or abs(x1 - x2) == a:
    if abs(y1 - y2) == a and abs(x1 - x2) == a:
        if r1 + r2 > abs(x1 - x2) and r1 + r2 > abs(y1 - y2):
            if abs(y1 - y2) == math.sqrt((r1 + r2) ** 2 - (x2 - x1) ** 2) or abs(x1 - x2) == math.sqrt(
                    (r1 + r2) ** 2 - (y2 - y1) ** 2):
                plt.title('Окружности имеют внешнее касание', fontsize=8, color='red')
            elif abs(y1 - y2) > math.sqrt((r1 + r2) ** 2 - (x2 - x1) ** 2) or abs(x1 - x2) > math.sqrt(
                    (r1 + r2) ** 2 - (y2 - y1) ** 2):
                plt.title('Окружности лежат одна вне другой, не касаясь', fontsize=8, color='red')
            elif math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) < r1 + r2:
                plt.title('Окружности пересекаются', fontsize=8, color='red')
            elif math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) > r1 + r2:
                plt.title('Окружности не пересекаются', fontsize=8, color='red')
            else:
                plt.title('Окружности имеют внутреннее касание', fontsize=8, color='red')
    else:
        if r1 + r2 > abs(x1 - x2) and r1 + r2 > abs(y1 - y2):
            if abs(y1 - y2) == math.sqrt((r1 + r2) ** 2 - (x2 - x1) ** 2) or abs(x1 - x2) == math.sqrt(
                    (r1 + r2) ** 2 - (y2 - y1) ** 2):
                plt.title('Окружности имеют внешнее касание', fontsize=8, color='red')
            elif abs(y1 - y2) > math.sqrt((r1 + r2) ** 2 - (x2 - x1) ** 2) or abs(x1 - x2) > math.sqrt(
                    (r1 + r2) ** 2 - (y2 - y1) ** 2):
                plt.title('Окружности лежат одна вне другой, не касаясь', fontsize=8, color='red')
            elif math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) < r1 + r2:
                plt.title('Окружности пересекаются', fontsize=8, color='red')
            elif math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) > r1 + r2:
                plt.title('Окружности не пересекаются', fontsize=8, color='red')
        elif r1 + r2 <= abs(x1 - x2) or r1 + r2 <= abs(y1 - y2):
            plt.title('Окружности не пересекаются', fontsize=8, color='red')
elif abs(y1 - y2) < a or abs(x1 - x2) < a:
    if r1 + r2 > abs(x1 - x2) and r1 + r2 > abs(y1 - y2):
        if math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) < r1 + r2:
            plt.title('Окружности пересекаются', fontsize=8, color='red')
        elif math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) < max(r1, r2):
            plt.title('Одна окружность лежит внутри другой, не касаясь', fontsize=8, color='red')
    else:
        plt.title('Одна окружность лежит внутри другой, не касаясь', fontsize=8, color='red')
plt.show()
