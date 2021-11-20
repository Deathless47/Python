'''
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
'''
import random


def median(data):
    for i in data:
        num = i
        a = 0
        for j in data:
            if i < j:
                a += 1
        if len(data) == 2 * a + 1:
            return num

def gnome(data_):
    i, j, size = 1, 2, len(data_)
    while i < size:
        if data_[i - 1] <= data_[i]:
            i, j = j, j + 1
        else:
            data_[i - 1], data_[i] = data_[i], data_[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return data_

m = 9
array = [random.randint(1, 50) for i in range(2 * m + 1)]

print(f'Исходный массив: {array}')
print(f'Медиана исходного массива: {median(array)}')
print(f'Отсортированный массив: {gnome(array)}')