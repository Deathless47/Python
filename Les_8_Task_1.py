'''
1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
'''
import hashlib


def func(string):
    sum_substring = set()
    for i in range(len(string)):
        for j in range(len(string), i, - 1):
            hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            sum_substring.add(hash_str)
    return len(sum_substring) - 1


my_string = input('Введите строку: ')
print(f'Подстрок в строке {my_string}: {func(my_string)}')

