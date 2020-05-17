# 5. Пользователь вводит номер буквы в алфавите. 
# Определить, какая это буква.

num = int(input('Введите номер буквы английского алфавита (от 1 до 26): '))
if 1 <= num <= 26:
    first_letter = ord('a')
    target_letter = chr(first_letter + num - 1)
    print('По номеру {} находится буква {}'.format(num, target_letter))
else:
    print('Буквы по номеру {} нет в алфавите'.format(num))

