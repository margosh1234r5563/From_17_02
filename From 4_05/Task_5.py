with open('input_5') as f:
    with open('output_5', 'w') as m:
        try:
            k = 0
            k = int(f.readline().replace('\n', '')) / int(f.readline().replace('\n', '')) + int(
                f.readline().replace('\n', ''))
            m = m.write(k)
        except ValueError:
            m = m.write('data error')
        except ZeroDivisionError:
            m = m.write('division by 0')
