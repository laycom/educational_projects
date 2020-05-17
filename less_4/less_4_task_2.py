# 2. Написать два алгоритма нахождения i-го по счёту простого числа. 
# Функция нахождения простого числа должна принимать на вход натуральное 
# и возвращать соответствующее простое число. 
# Проанализировать скорость и сложность алгоритмов.

def sieve(num):
    n = 10000
    nums = [i for i in range(n)]
    nums[1] = 0

    for i in range(2, n):
        if nums[i] != 0:
            j = i * 2
            
            while j < n:
                nums[j] = 0
                j += i
    result = [i for i in nums if i != 0]
    return result[num - 1]
    
def classic(num):
    n = 10000
    simple = []
    for i in range(2, n):
        for j in simple:
            if i % j == 0:
                break
        else:
            simple.append(i)
            if len(simple) == num:
                return simple[-1]
            
            
"""
ess_4_task_2.sieve(10)
500 loops, best of 5: 5.98 msec per loop

ess_4_task_2.sieve(100)
500 loops, best of 5: 6.01 msec per loop

ess_4_task_2.sieve(500)
500 loops, best of 5: 5.9 msec per loop

ess_4_task_2.sieve(700)
500 loops, best of 5: 5.89 msec per loop


ess_4_task_2.classic(10)
500 loops, best of 5: 9.07 usec per loop

ess_4_task_2.classic(100)
500 loops, best of 5: 496 usec per loop

ess_4_task_2.classic(500)
500 loops, best of 5: 13.6 msec per loop

ess_4_task_2.classic(700)
500 loops, best of 5: 25.7 msec per loop
"""

"""
    Для определения n-го простого числа невозможно однозначно задать диапазон чисел. 
Я в своем решении создавал список размером 10000.
         sieve          classic    сооотношение
10      5.98 msec     9.07 usec       0.0015
100     6.01 msec      496 usec       0.0825
380     5.87 msec     6.04 msec       1.029
500     5.90 msec     13.6 msec       2.305
700     5.89 msec     25.7 msec       4.363


    Решето Эратосфена выполняется одно и тоже колличество времени вне зависимости от числа которое мы ищем,
т.к. изначально работаем со всем массивом.
    Классический же метод увеличивает свое время работы в зависимости от искомого числа. 
    При поиске чисел до 380-го классический метод работает быстрее, дальше начинает выигрывать Решето Эратосфена.
"""