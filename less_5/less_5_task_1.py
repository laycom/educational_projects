# 1. Пользователь вводит данные о количестве предприятий, 
# их наименования и прибыль за четыре квартала для каждого предприятия. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) 
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import OrderedDict

num = int(input('Введите количество предприятий: '))
companies = OrderedDict()
sum = 0
companies_winner = {}
companies_loser = {}


for i in range(num):
    name = input('Введите наименование предприятия: ')
    profit = input('Введите прибыль за 4 квартала (через пробел): ').split()
    if len(profit) != 4:
        while len(profit) != 4:
            print('Необъодимо ввести прибыль за 4 квартала!')
            profit = input('Введите прибыль за 4 квартала (через пробел): ').split()
    companies[name] = profit
    
for key, values in companies.items():
    sum_local = 0
    for value in values:
        sum_local += int(value)
    sum += sum_local
    companies[key].append(sum_local)
    
sum = sum / num

for key, values in companies.items():
    if companies[key][-1] >= sum:
        companies_winner[key] = companies[key][4]
    else:
        companies_loser[key] = companies[key][4]
        
print()
print('-' * 50)        
print(f'Средняя прибыль всех предприятий за год: {sum}') 
print('-' * 50)    
print(' Компании у которых прибыль выше средней:')
print()
print(' наименование |  средняя прибыль  ')
print('-' * 50)     
for key, values in companies_winner.items():
    print(f' {key:^9}    |     {values:^8}')
    
print()
print('-' * 50)    
print(' Компании у которых прибыль ниже средней:')
print()
print(' наименование |  средняя прибыль  ')
print('-' * 50)     
for key, values in companies_loser.items():
    print(f' {key:^9}    |     {values:^8}') 
    
    
    