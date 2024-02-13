weight_f = float(input('Введите ваш вес в фунтах: '))
high_d = float(input('Введите ваш рост в дюймах: '))
weight_kg = weight_f * 0.4535923745
high_m = high_d * 0.0254
IMT = weight_kg / (high_m * high_m)
print(round(IMT, 2))
