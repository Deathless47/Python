'''
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
'''

'''
Спасибо за видео со спойлером, это практически как писать код используя диаграммы, 
которыми пользовались на первых уроках)))
'''

import random


def merge_sorted_(data):
    if len(data) <= 1:
        return data
    left = merge_sorted_(data[:len(data) // 2]) # из спойлера(видео в конце урока - разбить на 2 части) - левая
    right = merge_sorted_(data[len(data) // 2:]) # из спойлера(видео в конце урока - разбить на 2 части) - правая
    i = 0
    j = 0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            data[i + j] = left[i]
            i += 1
        else:
            data[i + j] = right[j]
            j += 1
    while len(left) > i:
        data[i + j] = left[i]
        i += 1
    while len(right) > j:
        data[i + j] = right[j]
        j += 1
    return data


array = [round(random.uniform(1, 50,), 3) for i in range(10)]
print(f'Исходный массив: {array}')

merge_sorted_(array)
print(f'Отсортированный массив: {array}')