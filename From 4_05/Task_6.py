with open('input_6', 'r') as f:
    with open('output_6', 'w') as m:
        try:
            k = 0
            k = int(f.readline())
            counter = 0
            for line in f.readlines():
                counter += 1
            if counter == k:
                m = m.write('YES')
            else:
                m = m.write('NO')
        except ValueError:
            m = m.write('ERROR')
