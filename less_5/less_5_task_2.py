# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. 
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict

def summary(num_1, num_2):
    result_list = []
    num_1 = num_1[::-1]  
    num_2 = num_2[::-1]
    if len(num_1) > len(num_2): 
        num_2 = num_2 + '0' * (len(num_1) - len(num_2))
    else:
        num_1 = num_1 + '0' * (len(num_2) - len(num_1))
    mind = 0
    for index, digit in enumerate(num_1):
        result = converter[digit] + converter[num_2[index]] + mind
        if result > 16: 
            mind = 1
        else:
            mind = 0
        current_result = result - 16 * mind
        result = converter_reverse[str(current_result)]
        result_list.append(result)
    return list(reversed(result_list))


def multiplication(num_1, num_2):
    num_1 = num_1[::-1]  
    num_2 = num_2[::-1]
    list_of_results = []

    for index, digit_2 in enumerate(num_2):
        result_middle_list = []
        mind = 0
        for digit in num_1:
            result_middle = converter[digit] * converter[digit_2] + mind
            if result_middle > 16:
                mind = result_middle // 16
            else:
                mind = 0
            current_result = result_middle - 16 * mind
            result = converter_reverse[str(current_result)]
            result_middle_list.append(result)
        if mind != 0:
            result_middle_list.append(str(mind))
        var_1 = list(reversed(result_middle_list))
        for j in range(index):  
            var_1.append('0')
        list_of_results.append(var_1) 
    for var_2 in range(0, len(list_of_results) - 1, 1):
        number_first = ''.join(list_of_results[var_2])
        number_second = ''.join(list_of_results[var_2 + 1])
        calculation_result = summary(number_first, number_second)
        list_of_results[var_2+1] = calculation_result

    return list_of_results[len(list_of_results)-1]



converter = defaultdict(list,
                        {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                         '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
                         )

converter_reverse = defaultdict(list,
                                {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', 
                                 '6': '6', '7': '7', '8': '8', '9': '9', '10': 'A', '11': 'B', 
                                 '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
                                 )

number_1 = input('Введите первое число: ')
number_2 = input('Введите второе число: ')
print('Сумма чисел:', summary(number_1, number_2))
print('Произведение чисел:', multiplication(number_1, number_2))

