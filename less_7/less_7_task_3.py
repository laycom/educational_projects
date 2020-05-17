# 3. Массив размером 2m + 1, где m — натуральное число, 
# заполнен случайным образом. Найдите в массиве медиану. 
# Медианой называется элемент ряда, делящий его на две равные части: 
# в одной находятся элементы, которые не меньше медианы, 
# в другой — не больше медианы.

import random
m = 5

array = [random.randint(0, 100) for i in range(2 * m + 1)]

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        q = random.choice(array)
        less = []
        more = []
        equally = []
        for item in array:
            if item > q:
                more.append(item)
            elif item < q:
                less.append(item)
            elif item == q:
                equally.append(item)
            else:
                print('Unknown error')
        return quicksort(less) + equally + quicksort(more)

def mediana(array):
    sort_array = quicksort(array)
    half = len(array) // 2
    if len(array) % 2 != 0:
        return sort_array[half]
    else:
        return round((sort_array[half] + sort_array[half - 1]) / 2, 2)


print(array)
print(quicksort(array))
print(mediana(array))