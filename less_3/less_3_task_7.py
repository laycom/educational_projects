# 7. В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

test_list = [random.randint(-20, 50) for _ in range(100)]

min = test_list[0]
index_min = 0


for i, num in enumerate(test_list):
    if num < min:
        min = num
        index_min = i
        
# Присваиваем значение второму наименьшему элементу
# отличное от найденного минимального        
if index_min != 0:
    min_2 = test_list[0]
    index_min_2 = 0
else:
    min_2 = test_list[1]
    index_min_2 = 1
       
for i, num in enumerate(test_list):
    if num < min_2 and i != index_min:
        min_2 = num
        index_min_2 = i
        
print(f'Исходный список {test_list}')
print(f'Наименьшие элементы: {min} по индексу {index_min}')
print(f'                     {min_2} по индексу {index_min_2}')