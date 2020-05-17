# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.


import random

size = 5
data = [[random.randint(0, 100) for _ in range(size)] for _ in range(size)]
max_of_min = [0][0]

for row in range(size):
    min = data[row][0]
    index_min = [row, 0]
    for col in range(1, size):
        if data[row][col] < min:
            min = data[row][col]
            index_min = [row, col]
    if row == 0:
        max_of_min = min
        index_max_of_min = index_min
    elif max_of_min < min:
        max_of_min = min
        index_max_of_min = index_min
    
        
for row in data:
    for col in row:
        print(f'{col:>3}', end='')
    print()

print('Максимальный элемент среди минимальных элементов ' 
     f'столбцов матрицы {max_of_min} ({index_max_of_min})')