for i in range(10, 99 + 1):
    if ((i * i) // 10 % 10 == i // 10 and (i * i) % 10 % 10 == i % 10 and i * i > 100
            and i * i < 1000):
        print(i)
