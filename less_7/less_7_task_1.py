# 1. Отсортируйте по убыванию методом пузырька 
# одномерный целочисленный массив, заданный 
# случайными числами на промежутке [-100; 100). 
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, 
# которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, 
# но помните, что у вас должна остаться сортировка пузырьком. 
# Улучшенные версии сортировки, например, расчёской, 
# шейкерная и другие в зачёт не идут.


import random
size = 10
array = [random.randint(-100, 100) for i in range(size)]
array2 = array[:]
print(array)
print()

# Данный алгоритм чуть улучшен, цикл работает до тех пор пока 
# происходят перестановки
# в результате уменьшается цисло итераций цикла

def bubble_sort(array):
    n = 1
    count = 0
    swap = True
    while swap and n < len(array):
        swap = False
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True
        count += 1
        n += 1
        print(array)
    print(count)
    
def bubble_sort2(array):
    n = 1
    count = 0
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        count += 1
        n += 1
        print(array)
    print(count)
        
bubble_sort(array)
print()
bubble_sort2(array2)
