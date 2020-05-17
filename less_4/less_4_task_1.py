# 1. Проанализировать скорость и сложность одного любого алгоритма 
# из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом 
# (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

# Определить, какое число в массиве встречается чаще всего.

import random
import timeit
import cProfile
num_list = [random.randint(-10, 50) for _ in range(10000)]


def max_method(size, num_list=num_list):
    test_list = num_list[:size]
    max_meets = {}
    max_list = []
    for item in test_list:
        if item not in max_meets:
            max_meets[item] = test_list.count(item)
    max_val = max(max_meets.values())
    final_dict = {key: value for key, value in max_meets.items() if value == max_val}
    return list(final_dict.items())[0]
    

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
    return key_max, max

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
    return key_max, max
        
"""
less_4_task_1.max_method(100)"
1000 loops, best of 5: 96.6 usec per loop

less_4_task_1.max_method(500)"
1000 loops, best of 5: 596 usec per loop

less_4_task_1.max_method(1000)
1000 loops, best of 5: 1.24 msec per loop

less_4_task_1.max_method(5000)
1000 loops, best of 5: 6.37 msec per loop

less_4_task_1.max_method(10000)
1000 loops, best of 5: 12.7 msec per loop


less_4_task_1.max_dict(100)"
1000 loops, best of 5: 234 usec per loop

less_4_task_1.max_dict(500)"
1000 loops, best of 5: 1.47 msec per loop

less_4_task_1.max_dict(1000)
1000 loops, best of 5: 2.93 msec per loop

less_4_task_1.max_dict(5000)
1000 loops, best of 5: 14.4 msec per loop

less_4_task_1.max_dict(10000)
1000 loops, best of 5: 29.6 msec per loop


less_4_task_1.max_round(100)"
1000 loops, best of 5: 469 usec per loop

less_4_task_1.max_round(500)"
1000 loops, best of 5: 11.6 msec per loop

less_4_task_1.max_round(1000)"
1000 loops, best of 5: 45.8 msec per loop
"""

def data_print():
    print('  size    |   max_method   |   max_dict     |   max_round    |')
    print('-' * 62)

    data = {'100': ['96.6 usec', '234 usec', '469 usec'],
            '500': ['596 usec', '1.47 msec', '11.6 msec'],
            '1000': ['1.24 msec', '2.93 msec', '45.8 msec'],
            '5000': ['6.37 msec', '14.4 msec', '???'],
            '10000': ['12.7 msec', '29.6 msec', '???']}
            

    for key, values in data.items():
        print(f'  {key:<6}  |', end=' ')
        for value in values:
            print(f'{value:^13}  |', end=' ')
        print()
# Запусти data_print() чтобы увидеть результаты

""" 
    По результатам мы видем что наиболее быстро работает метод использующий 
втсроенные  фунцкции и хранящий данные о посчитанных числах в словаре.
    Метод использующий подсчет вручную и также хранящий данные о посчитанных 
числах в словаре работает в среденм в 2,3 -2,5 раза медленее
    Метод перебора всех элементов без хранения данных о уже подсчитанных числах 
занимает гораздо больше времени и скорость его работы замедляется нелинейно

        max_method    max_round   сооотношение
100     96.6 usec      469 usec       4,85
500      596 usec     11.6 msec      19,46
1000    1.24 msec     45.8 msec      36,93
5000    6.37 msec          *            *

* примерно через час работы отчаялся и прервал выполнение
""" 