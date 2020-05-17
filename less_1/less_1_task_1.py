# 1. Выполнить логические побитовые операции 
# «И», «ИЛИ» и др. над числами 5 и 6. 
# Выполнить над числом 5 побитовый сдвиг 
# вправо и влево на два знака.

first_num = 5
second_num = 6

print(f'Логическое "И":  {bin(first_num & second_num)}, {first_num & second_num}')
print(f'Логическое "ИЛИ":  {bin(first_num | second_num)}, {first_num | second_num}')
print(f'"Исключающее ИЛИ":  {bin(first_num ^ second_num)}, {first_num ^ second_num}')
print(f'"Побитовый сдвиг числа 5 влево на 2 знака" {bin(first_num << 2)}, {first_num << 2}')
print(f'"Побитовый сдвиг числа 5 вправо на 2 знака" {bin(first_num >> 2)}, {first_num >> 2}')



