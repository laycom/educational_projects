# 9. Среди натуральных чисел, которые были введены, 
# найти наибольшее по сумме цифр. 
# Вывести на экран это число и сумму его цифр.

num = int(input('Введите количество чисел: '))
max = 0
sum_max = 0

for i in range(num):
    value = int(input('Введите число: '))
    sum = 0
    value_work = value
    for i in range(len(str(value_work))):
        sum += value_work % 10
        value_work //= 10 
    if sum_max < sum:
        sum_max = sum
        max = value
print(f'В числе {max}, наибольшая сумма цифр: {sum_max} ')