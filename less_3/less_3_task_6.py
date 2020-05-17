# 6. В одномерном массиве найти сумму элементов, 
# находящихся между минимальным и максимальным элементами. 
# Сами минимальный и максимальный элементы в сумму не включать.

import random

test_list = [random.randint(-100, 100) for _ in range(10)]

max = test_list[0]
index_max = 0
min = test_list[0]
index_min = 0
sum = 0

for i, num in enumerate(test_list):
    if num > max:
        max = num
        index_max = i
    if num < min:
        min = num
        index_min = i
        
if index_min > index_max:
    index_min, index_max = index_max, index_min
    
for num in range(index_min + 1, index_max):
    sum += test_list[num]
    
print(f'Исходный список {test_list}')
print(index_min, index_max)
print(f'Сумма элементов равна {sum} ({index_min}:{index_max})')