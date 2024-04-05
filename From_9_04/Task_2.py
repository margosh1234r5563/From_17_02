letter = input()
for i in range(len(letter)):
    if (i + 1) % 3 == 0:
        print(letter[i], end='')
