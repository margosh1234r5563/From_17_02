with open('input_8') as f:
    with open('output_8', 'w') as m:
        k = ''

        # январь 31
        s = 0
        for x in range(1, 32):
            s += int(f.readline())
        s = s / 31
        k += str(s) + '\n'

        # февраль 28
        s = 0
        for x in range(1, 29):
            s += int(f.readline())
        s = s / 28
        k += str(s) + '\n'

        # март 31
        s = 0
        for x in range(1, 32):
            s += int(f.readline())
        s = s / 31
        k += str(s) + '\n'

        # апрель 30
        s = 0
        for x in range(1, 31):
            s += int(f.readline())
        s = s / 30
        k += str(s) + '\n'

        # май 31
        s = 0
        for x in range(1, 32):
            s += int(f.readline())
        s = s / 31
        k += str(s) + '\n'

        # июнь 30
        s = 0
        for x in range(1, 31):
            s += int(f.readline())
        s = s / 30
        k += str(s) + '\n'

        # июль 31
        s = 0
        for x in range(1, 32):
            s += int(f.readline())
        s = s / 31
        k += str(s) + '\n'

        # август 31
        s = 0
        for x in range(1, 32):
            s += int(f.readline())
        s = s / 31
        k += str(s) + '\n'

        # сентябрь 30
        s = 0
        for x in range(1, 31):
            s += int(f.readline())
        s = s / 30
        k += str(s) + '\n'

        # октябрь 31
        s = 0
        for x in range(1, 32):
            s += int(f.readline())
        s = s / 31
        k += str(s) + '\n'

        # ноябрь 30
        s = 0
        for x in range(1, 31):
            s += int(f.readline())
        s = s / 30
        k += str(s) + '\n'

        # декабрь 31
        s = 0
        for x in range(1, 32):
            s += int(f.readline())
        s = s / 31
        k += str(s) + '\n'

        m.write(k)
