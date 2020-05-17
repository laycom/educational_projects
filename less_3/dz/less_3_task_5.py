# 5. В массиве найти максимальный отрицательный элемент. 
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» 
# и «максимальный отрицательный». Это два абсолютно разных значения.

import random
test_list = [random.randint(-10, 50) for _ in range(10)]

max_negative = 0
max_negative_index = -1

for i, num in enumerate(test_list):
    if num < 0:
        if max_negative_index == -1:
            max_negative = num
            max_negative_index = i
        if max_negative < num:
            max_negative = num
            max_negative_index = i


print(f'Исходный список {test_list}')               
if max_negative_index == -1:
    print('В списке нет отрицательных чисел')
else:      
    print(f'Максимальный отрицательный элемент {max_negative}, его позиция в списке {max_negative_index}')