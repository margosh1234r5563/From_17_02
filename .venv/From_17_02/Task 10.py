#Task 10
number_r=input('Введите номер рейса: ')
r_name_company=input('Введите название авиакомпании (на русском языке): ')
e_name_company=input('Введите название авиакомпании (на английском языке): ')
r_fly_city=input('Введите rород прилета (на русском языке): ')
e_fly_city=input('Введите rород прилета (на английском языке): ')

print('номер рейса:',number_r)
print('название авиакомпании (на русском языке):',r_name_company)
print('название авиакомпании (на английском языке):',e_name_company)
print('rород прилета (на русском языке):',r_fly_city)
print('rород прилета (на английском языке):',e_fly_city)
print('Заканчивается посадка на рейс',number_r,r_name_company,'до',r_fly_city)
print('This is the final boarding call for',e_name_company,'flight', number_r,'to',e_fly_city)