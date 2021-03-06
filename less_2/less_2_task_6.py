# 6. В программе генерируется случайное целое число от 0 до 100. 
# Пользователь должен его отгадать не более чем за 10 попыток. 
# После каждой неудачной попытки должно сообщаться, больше или 
# меньше введенное пользователем число, чем то, что загадано. 
# Если за 10 попыток число не отгадано, вывести ответ.

from random import randint

num = randint(0, 100)
for i in range(0, 10):
    user_num = int(input('Введите число от 0 до 100: '))
    if user_num == num:
        print(f'Вы отгадали число! Число {num}')
        break 
    elif user_num > num:
        print('Введенное число больше загаданного')
    else:
        print('Введенное число меньше загаданного')
else:
    print(f'Вы проиграли, загаданное число {num}')