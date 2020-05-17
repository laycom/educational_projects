# 2. Посчитать четные и нечетные цифры введенного 
# натурального числа. Например, если введено число 34560, 
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите число: '))
num_out = num
count_even = 0
count_odd = 0
while num != 0:
    if num % 2 == 0:
        count_even += 1
        num //= 10
    else:
        count_odd += 1
        num //= 10
print(f'В числе {num_out}: четных чисел {count_even}, нечетных чисел {count_odd}')