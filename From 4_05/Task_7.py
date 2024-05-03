with open('input_7') as f:
    with open('output_7', 'w') as m:
        k = ''
        for line in f:
            if line != '100\n':
                k += line
        m = m.write(k)
