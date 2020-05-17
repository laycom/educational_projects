# 8. Матрица 5x4 заполняется вводом с клавиатуры, 
# кроме последних элементов строк. 
# Программа должна вычислять сумму введенных элементов 
# каждой строки и записывать ее в последнюю ячейку строки. 
# В конце следует вывести полученную матрицу.

size = 4
data = [[0] * 5 for _ in range(4)]
for row in range(size):
    sum = 0
    for col in range(size):
        data[row][col] = int(input('Введите число: '))
        sum += data[row][col]
    data[row][size] = sum
    
for row in data:
    print(row)
    