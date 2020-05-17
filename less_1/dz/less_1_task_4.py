# 4. Пользователь вводит две буквы. 
# Определить, на каких местах алфавита они стоят, 
# и сколько между ними находится букв.


letter_1 = ord(input('Введите первую букву от "a" до "z": '))
letter_2 = ord(input('Введите вторую букву от "a" до "z": '))

first_letter = ord('a')

letter_1_position = letter_1 - first_letter + 1
letter_2_position = letter_2 - first_letter + 1
distance = abs(letter_2_position - letter_1_position - 1)
print('Буква {} --> место в алфавите {}'.format(chr(letter_1), letter_1_position))
print('Буква {} --> место в алфавите {}'.format(chr(letter_2), letter_2_position))
print('Между {} и {} находится {} букв(ы)'.format(chr(letter_1), chr(letter_2), distance))