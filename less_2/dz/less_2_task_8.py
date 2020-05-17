# 8. Посчитать, сколько раз встречается определенная цифра 
# в введенной последовательности чисел. 
# Количество вводимых чисел и цифра, 
# которую необходимо посчитать, задаются вводом с клавиатуры.

num = int(input('Введите количество чисел: '))
target_num = int(input('Введите число для поиска: '))
count = 0
for i in range(num):
    value = int(input('Введите число: '))
    for i in range(len(str(value))):
        if value % 10 == target_num:
            count += 1
            value //= 10
        else:
            value //= 10 
            
            
print(f'Число {target_num} встречалось {count} раз(а)')