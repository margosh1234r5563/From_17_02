n = int(input())


def task_2(n):
    if n <= 10:
        result = n - 1
    elif n <= 190:  # 10 (из пред условия) + 20 * 9 (от 10 до 99), будем начинать отсчет с n-10 для удобства (считаем с 1)
        if (n - 10) % 2 != 0:  # разряд десятков
            result = int((n - 10) / 20) + int((n - 10) / 20 % 2 != 0)
            # В каждой десятке чисел (например 10-19) 20 цифр, поэтому / 20 для отделения разряда десятков (/2 чтобы из 180 цифр почучить 90 чисел и /10 для десятков)
            # Если число в разряде десятков четное, то все ок, если нет, то нужно после целочисленного деления прибавить 1
            # (если номер начинается с 2, то 2 % 2 = 0, ничего не нужно, если с 1, то 1 % 2 = 1 прибавляем единицу)
        else:  # разряд единиц
            result = int((n - 10) / 2 % 10 - int((n - 10) / 2 % 10 != 0)) + 9 * int((n - 10) / 2 % 10 == 0)
            # Аналогично делим на два для перехода к 90 числам, отделяем разряд единиц взятием остатка
            # полученная цифра всегда на 1 больше нужной кроме одного случая с 0. там должно выйти 9, но мы оперируем одноразрядными числами, поэьлму не можеи полоучить 10-1
            # Два последних слагаемых своими проверками на 0 в остатке решают эту проблему, мы не отнимаем 1 и прибавляем 9
    else:
        if (n - 190) % 3 == 2:  # разряд десятков
            result = int((n - 190) % 100 / 30)
        elif (n - 190) % 3 == 1:  # разряд сотен
            result = int((n - 190) / 300) + int((
                                                        n - 190) % 3 != 0)  # Аналогично случаю с двузначными числами с оговоркаой на то что в диапазоне 110-119 теперь 30 цифр
        else:  # разряд единиц
            result = int((n - 190) / 3 % 10) - int((n - 190) / 3 % 10 != 0) + 9 * int(
                (n - 190) / 3 % 10 == 0)  # Аналогично случаю с двузначными числами
    print(result)
    return result


task_2(n)