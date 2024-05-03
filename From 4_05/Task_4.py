with open('input_3', 'r') as f:
    k = ''
    for line in f.readlines():
        line = line.replace('\n', '')
        if len(line) > 20:
            k += line + '\n'
with open('output_3', 'w') as m:
    m = m.write(k)
