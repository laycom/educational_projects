# 1. Подсчитать, сколько было выделено памяти под переменные 
# в ранее разработанных программах в рамках первых трех уроков. 
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) 
# вставить в виде комментариев в файл с кодом. Не забудьте указать версию и 
# разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.

# Определить, какое число в массиве встречается чаще всего.

import random
import timeit
import sys
num_list = [random.randint(-10, 50) for _ in range(10000)]

def program_size(*args):
    item_size = {}
    sum_size = 0
    for item in args:
        if str(type(item)) in item_size:
            item_size[str(type(item))] += sys.getsizeof(item)
        else:
            item_size[str(type(item))] = sys.getsizeof(item)
    for value in item_size.values():
        sum_size += value
    return item_size, sum_size
    
def size_print(key_max, max, item_size, name):
    print('Функция', name)
    print(f'Число {key_max} встречается {max} раз')
    for key, value in item_size[0].items():
        print(f'{key:<15}: {value}')
    
    print(f'Суммарный объем затраченной памяти = {item_size[1]}')
    print()


def max_method(size, num_list=num_list):
    test_list = num_list[:size]
    max_meets = {}
    for item in test_list:
        if item not in max_meets:
            max_meets[item] = test_list.count(item)
    max_val = max(max_meets.values())
    final_dict = {key: value for key, value in max_meets.items() if value == max_val}
    item_size = program_size(test_list, max_meets, item, max_val, final_dict)
    return list(final_dict.items())[0], item_size
    

def max_dict(size, num_list=num_list):
    test_list = num_list[:size]
    max_meets = {}
    max = 0
    for item in test_list:
        count = 0
        if item not in max_meets:
            for num in test_list:
                if item == num:
                    count += 1
            max_meets[item] = count

    for key, value in max_meets.items():
        if value > max:
            max = value
            key_max = key
    item_size = program_size(test_list, max_meets, max, count, item, 
                        num, key, value, key_max)
    return key_max, max, item_size

def max_round(size, num_list=num_list):
    test_list = num_list[:size]
    max = 0
    for item in test_list:
        count = 0
        for num in test_list:
            if item == num:
                count += 1
        if count > max:
            max = count
            key_max = item
    item_size = program_size(test_list, max, item, count, num, key_max)
    return key_max, max, item_size
        
key_max, item_size = max_method(10000)
key_max, max = key_max[0], key_max[1]
size_print(key_max, max, item_size, 'max_method')

key_max, max, item_size = max_dict(10000)
size_print(key_max, max, item_size, 'max_dict')

key_max, max, item_size = max_round(10000)
size_print(key_max, max, item_size, 'max_round')

"""
3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] win32

Функция max_method
Число 6 встречается 188 раз
<class 'list'> : 80056
<class 'dict'> : 2504
<class 'int'>  : 56
Суммарный объем затраченной памяти = 82616

Функция max_dict
Число 6 встречается 188 раз
<class 'list'> : 80056
<class 'dict'> : 2272
<class 'int'>  : 192
Суммарный объем затраченной памяти = 82520

Функция max_round
Число 6 встречается 188 раз
<class 'list'> : 80056
<class 'int'>  : 140
Суммарный объем затраченной памяти = 80196
"""

# по результатам видно что меньше всего занимает памяти max_round, но основной объем
# памяти занимают входные данные
    
    
