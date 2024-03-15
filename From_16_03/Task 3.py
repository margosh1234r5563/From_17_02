num = int(input())
first_letter = num // 1000
second_letter = num // 100 % 10
third_letter = num // 10 % 10 % 10
thour_letter = num % 10 % 10 % 10 % 10
if first_letter == thour_letter and second_letter == third_letter:
    print('настоящее')
else:
    print('кривое')
