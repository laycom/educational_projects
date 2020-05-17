# 1. В диапазоне натуральных чисел от 2 до 99 определить, 
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9. 
# Примечание: 8 разных ответов.

test_list = [item for item in range(2, 100)]

output = {item: [] for item in range(2, 10)}

for item in test_list:
    for num in range(2, 10):
        if item % num == 0:
            output[num].append(item)
            
for key, value in output.items():
    print('Количество чисел кратных {}: {}'.format(key, len(value)))
    
