with open('input_9') as f:
    k = ''
    i = 1
    for line in f.readlines():
        if i % 2 == 0:
            k += line
        i += 1
with open('output_9', 'w') as m:
    m = m.write(k)
