# 2. Отсортируйте по возрастанию методом слияния 
# одномерный вещественный массив, заданный случайными числами 
# на промежутке [0; 50). 
# Выведите на экран исходный и отсортированный массивы.

import random


size = 10
array = [round(random.random() * 50, 2) for i in range(size)]



def merge_sort(array):

    if len(array) == 1:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    else:
        result = []
        middle = int(len(array) / 2)
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

print(array)            
print('Ответ', merge_sort(array))

                
                