first_answer = input('Собака короткошерстной породы? ')
if first_answer == 'да':
    second_answer = input('Рост собаки менее 50 см? ')
    if second_answer == 'да':
        third_answer = input('У собаки короткий хвост? ')
        if third_answer == 'да':
            print('английский бульдог')
        else:
            thour_answer = input('У собаки длинные уши? ')
            if thour_answer == 'да':
                print('гончая')
            else:
                five_answer = input('У собаки короткое тело? ')
                if five_answer == 'да':
                    print('мопс')
                else:
                    print('чихуахуа')
    else:
        third_answer = input('Собака весит более 50 кг? ')
        if third_answer == 'да':
            print('датский дог')
        else:
            print('фоксхаунд')
else:
    second_answer = input('Рост собаки менее 50 см? ')
    if second_answer == 'да':
        third_answer = input('У собаки доброжелательный характер? ')
        if third_answer == 'да':
            print('кокер-спаниэль')
        else:
            print('ирландский сеттер')
    else:
        third_answer = input('У собаки рост менее 70 см? ')
        if third_answer == 'да':
            thour_answer = input('У собаки длинные уши? ')
            if thour_answer == 'да':
                print('большой вандейский грифон')
            else:
                print('колли')
        else:
            thour_answer = 'Окрас рыжий с белыми отметинами? '
            if thour_answer == 'да':
                print('сенбернар')
            else:
                five_answer = input('Белоснежный окрас? ')
                if five_answer == 'да':
                    print('ирландский волкодав')
                else:
                    print('ньюфаунленд')
