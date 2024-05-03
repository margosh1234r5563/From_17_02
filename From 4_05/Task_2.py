with open('input_1') as f:
    k = ''
    for line in f.readlines():
        if line[0] == 'a' or line[0] == 'A':
            k += line
with open('output_1', 'w') as m:
    m.write(k)
