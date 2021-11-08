'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
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

array[res_max_], array[res_min_] = array[res_min_], array[res_max_]

print(f'Мой новый массив: {array}')



