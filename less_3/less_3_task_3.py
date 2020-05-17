# 3. В массиве случайных целых чисел 
# поменять местами минимальный и максимальный элементы.

import random

test_list = [random.randint(-100, 100) for _ in range(10)]

max = test_list[0]
index_max = 0
min = test_list[0]
index_min = 0

for i, num in enumerate(test_list):
    if num > max:
        max = num
        index_max = i
    if num < min:
        min = num
        index_min = i
        
print(f'Исходный список        {test_list}')

spam = test_list[index_max]
test_list[index_max] = test_list[index_min]
test_list[index_min] = spam
        
 
print(f'Преобразованный список {test_list}')