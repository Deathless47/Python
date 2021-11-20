'''
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
'''

import random


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
        print(f'Отсортированный массив: {array}')

array = [random.randint(-100, 100) for i in range(10)]
print(f'Исходный массив:{array}')

bubble_sort(array)


'''
Для тог чтобы убрать лишние массивы и в конце вывести только один отсортированный массив
'''

print('*' * 75)

def sort_2(array_2):
    n = 1
    while n < len(array_2):
        sorted_ = True
        for i in range(len(array_2) - 1):
            if array_2[i] < array_2[i + 1]:
                array_2[i], array_2[i + 1] = array_2[i + 1], array_2[i]
                sorted_ = False
        if sorted_ == True:
            break
        n += 1
    print(f'Отсортированный массив 2: {array_2}')


array_2 = [random.randint(-100, 100) for i in range(10)]
print(f'Исходный массив 2:{array_2}')

sort_2(array_2)
