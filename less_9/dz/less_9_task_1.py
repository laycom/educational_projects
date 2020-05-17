# 1. Определение количества различных подстрок 
# с использованием хеш-функции. Пусть на вход функции дана строка. 
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * задача считается решённой, если в коде использована функция 
# вычисления хеша (hash(), sha1() или любая другая из модуля hashlib)

import hashlib

def search_lines(line):
    assert len(line) > 0, 'Строка пустая'
    length = len(line)
    hash = []
    unique_sub = []
    for i in range(length):
        for j in range(i + 1, length + 1):
            spam = hashlib.sha1(line[i:j].encode('utf-8')).hexdigest()
            if spam not in hash:
                if length != len(line[i:j]):
                    unique_sub.append(line[i:j])
                    hash.append(spam)
    return len(hash), unique_sub
    
    
# Функция принимает на вход строку, в случае если строка пустая выдает ошибку.
# Функция перебирает все возможные подстроки, считает их хеш и заносит все 
# уникальные хеш (переменная spam) в список hash. 
# На выходе функции для наглядности добавлен спискок всех уникальных подстрок
# unique_sub
    
num, unique_sub = search_lines('papa')
print(num)

print(unique_sub)