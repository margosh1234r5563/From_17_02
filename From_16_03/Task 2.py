import matplotlib.pyplot as plt

xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())

fig, ax = plt.subplots()

a = plt.Circle((xc, yc), r, fill=False)
b = plt.Circle((x, y), 2, linewidth=2, color='red')
ax.add_artist(b)
ax.add_artist(a)

plt.xlim(x - 100, x + 100)
plt.ylim(y - 100, y + 100)

if (x - xc) ** 2 + (y - yc) ** 2 < r ** 2:
    plt.text(xc - r + 30, yc - r - 8, 'Точка внутри окружности', color='red')
else:
    plt.text(xc - r + 30, yc - r - 8, 'Точка вне окружности', color='red')
plt.show()
