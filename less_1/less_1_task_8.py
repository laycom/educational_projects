# 8. Вводятся три разных числа. 
# Найти, какое из них является средним 
# (больше одного, но меньше другого).

num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
num_3 = float(input('Введите третье число: '))

if num_2 < num_1 < num_3 or num_3 < num_1 < num_2:
    print(f'Средним числом является {num_1}')
elif num_1 < num_2 < num_3 or num_3 < num_2 < num_1:
    print(f'Средним числом является {num_2}')
elif num_1 < num_3 < num_2 or num_2 < num_3 < num_1:
    print(f'Средним числом является {num_3}')
else:
    print('Неверные данные')