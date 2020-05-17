# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. 
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

from random import randint, random

print('Генерация случайного целого числа, введите границы диапазона: ')
start = int(input('Первое число: '))
end = int(input('Второе число: '))
if start > end:
    st = end
    end = start
    start = st
num = randint(start, end)

print(f'Случайное число от {start} до {end}: {num}')
print()

print('Генерация случайного вещественного числа, введите границы диапазона: ')
start = float(input('Первое число: '))
end = float(input('Второе число: '))
if start > end:
    st = end
    end = start
    start = st
num = random() * (end - start) + start

print('Случайное число от {} до {}: {:.2f}'.format(start, end, num))
print()

print('Генерация случайной буквы, введите границы диапазона: ')
start = ord(input('Первая буква: '))
end = ord(input('Вторая буква: '))
if start > end:
    st = end
    end = start
    start = st
num = int(random() * (end - start + 1)) + start

print('Случайная буква от {} до {}: {}'.format(chr(start), chr(end), chr(num)))
