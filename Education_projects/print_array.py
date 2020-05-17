# Преобразование списка со всеми вложенными списками в "однородный" список
# Например [1, 2, 3, [4, 5], 6, [7, [8, 9, [10]]], 11] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

array = [1, 2, 3, [4, 5], 6, [7, [8, 9, [10]]], 11]
output_array = []

def unpacking_array(list):
    if not list:
        print('Список пуст')
    for item in list:
        try:
            if len(item) >= 1:
                unpacking_array(item)
        except TypeError:
            output_array.append(item)
    return output_array

print(unpacking_array(array))