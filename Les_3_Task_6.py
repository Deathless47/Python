'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''

import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 25
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Мой случайный массив {array}')

max_ = array[0]
min_ = array[0]
for i in array:
    if i > max_:
        max_ = i
    elif i < max_ and i < min_:
        min_ = i

res_max_ = array.index(max_)
res_min_ = array.index(min_)

step = 1
summa = 0

if res_max_ < res_min_: # если максимальный элемент стоит раньше минимального
    step = -1

for i in array[res_min_ + step:res_max_:step]:
    summa += i

print(array[res_max_], array[res_min_]) # вывел чтобы показать мин и макс элементы для более легкой проверки
print(f'Сумма элементов: {summa}')






