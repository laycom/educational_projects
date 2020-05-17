# 4. Определить, какое число в массиве встречается чаще всего.


import random
test_list = [random.randint(0, 6) for _ in range(100)]

max_meets = {}
max = 0

# Вариант 1 создание словаря содержащего пары значений
# 'число': количество повторений в списке и дальнейший поиск
# максимума в созданном словаре 
for item in test_list:
    count = 0
    if item not in max_meets:
        for num in test_list:
            if item == num:
                count += 1
        max_meets[item] = count

for key , value in max_meets.items():
    if value > max:
        max = value
        key_max = key

# Вариант 2 поиск максимума сразу в цикле
# for item in test_list:
    # count = 0
    # for num in test_list:
        # if item == num:
            # count += 1
    # if count > max:
        # max = count
        # key_max = item
        
for i, num in enumerate(test_list):
    print(f'{num:<2}', end=' ')
    if (i + 1) % 20 == 0:
        print()

print(f'Чаще всего встречается число {key_max}: {max} раз(а)')   


            
    