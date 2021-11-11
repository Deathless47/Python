'''
1.	Проанализировать скорость и сложность одного любого алгоритма
из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
'''

'''
Задача - В массиве случайных целых чисел поменять местами минимальный и максимальный элементы (Урок 3 домашнее задание 3).
Здесь в качестве N выступает длина списка, брал значения 10, 50, 100, 1_000 и 10_000
'''

import timeit
import cProfile
import random


array = [random.randint(1, 1_000_000) for _ in range(10)]
#print(f'Мой случайный массив {array}') # оставил для проверки правильности работы вариантов кода небольшой длине списка
# в timeit и cProfile для анализа использовал разные значения длины списка

# вариант 1 решения задачи. Методом перебора

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
#print(f'Мой новый массив: {array}') # оставил для проверки правильности работы вариантов кода небольшой длине списка


print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(10)]', number=1000, globals=globals()))     # 0.005542499999999999
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(50)]', number=1000, globals=globals()))     # 0.027503899999999998
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(100)]', number=1000, globals=globals()))    # 0.0535108
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(1_000)]', number=1000, globals=globals()))  # 0.5380956
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(10_000)]', number=1000, globals=globals())) # 5.2768365


cProfile.run('array = [random.randint(1, 1_000_000) for _ in range(1000)]')
'''
 5045 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<listcomp>)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
     1000    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
     1000    0.000    0.000    0.001    0.000 random.py:290(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:334(randint)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1041    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

'''

cProfile.run('array = [random.randint(1, 1_000_000) for _ in range(10_000)]')
'''
 50450 function calls in 0.013 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.013    0.013 <string>:1(<listcomp>)
        1    0.000    0.000    0.013    0.013 <string>:1(<module>)
    10000    0.003    0.000    0.004    0.000 random.py:237(_randbelow_with_getrandbits)
    10000    0.004    0.000    0.009    0.000 random.py:290(randrange)
    10000    0.003    0.000    0.011    0.000 random.py:334(randint)
        1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10446    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

'''

cProfile.run('array = [random.randint(1, 1_000_000) for _ in range(100_000)]')
'''
  504846 function calls in 0.135 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.021    0.021    0.135    0.135 <string>:1(<listcomp>)
        1    0.000    0.000    0.135    0.135 <string>:1(<module>)
   100000    0.032    0.000    0.046    0.000 random.py:237(_randbelow_with_getrandbits)
   100000    0.043    0.000    0.088    0.000 random.py:290(randrange)
   100000    0.026    0.000    0.114    0.000 random.py:334(randint)
        1    0.000    0.000    0.135    0.135 {built-in method builtins.exec}
   100000    0.006    0.000    0.006    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   104842    0.008    0.000    0.008    0.000 {method 'getrandbits' of '_random.Random' objects}

'''


# вариант 2 решения задачию Через встроенные функции max, min

max_1_ = max(array)
min_1_ = min(array)
max_1_, min_1_ = min_1_, max_1_
#print(f'Мой новый массив: {array}') # оставил для проверки правильности работы вариантов кода небольшой длине списка


print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(10)]', number=1000, globals=globals()))     # 0.005596500000000226
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(50)]', number=1000, globals=globals()))     # 0.027084299999999395
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(100)]', number=1000, globals=globals()))    # 0.05356929999999949
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(1_000)]', number=1000, globals=globals()))  # 0.5259362000000003
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(10_000)]', number=1000, globals=globals())) # 5.382113499999999


cProfile.run('array = [random.randint(1, 1_000_000) for _ in range(1000)]')
'''
 5065 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<listcomp>)
        1    0.001    0.001    0.002    0.002 <string>:1(<module>)
     1000    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
     1000    0.000    0.000    0.001    0.000 random.py:290(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:334(randint)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1061    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
'''

cProfile.run('array = [random.randint(1, 1_000_000) for _ in range(10_000)]')
'''
50476 function calls in 0.013 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.013    0.013 <string>:1(<listcomp>)
        1    0.000    0.000    0.013    0.013 <string>:1(<module>)
    10000    0.003    0.000    0.004    0.000 random.py:237(_randbelow_with_getrandbits)
    10000    0.004    0.000    0.008    0.000 random.py:290(randrange)
    10000    0.003    0.000    0.011    0.000 random.py:334(randint)
        1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10472    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
'''

cProfile.run('array = [random.randint(1, 1_000_000) for _ in range(100_000)]')
'''
504957 function calls in 0.134 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.021    0.021    0.134    0.134 <string>:1(<listcomp>)
        1    0.000    0.000    0.134    0.134 <string>:1(<module>)
   100000    0.031    0.000    0.045    0.000 random.py:237(_randbelow_with_getrandbits)
   100000    0.042    0.000    0.087    0.000 random.py:290(randrange)
   100000    0.026    0.000    0.113    0.000 random.py:334(randint)
        1    0.000    0.000    0.134    0.134 {built-in method builtins.exec}
   100000    0.006    0.000    0.006    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   104953    0.008    0.000    0.008    0.000 {method 'getrandbits' of '_random.Random' objects}

'''


# вариант 3 решения задачи. Через встроенную функцию sorted

arr = sorted(array)
max_2_ = arr[-1]
min_2_ = arr[0]
max_2_, min_2_ = min_2_, max_2_
#print(f'Мой новый массив: {array}') # оставил для проверки правильности работы вариантов кода небольшой длине списка


print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(10)]', number=1000, globals=globals()))     # 0.006729899999999844
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(50)]', number=1000, globals=globals()))     # 0.026482099999999065
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(100)]', number=1000, globals=globals()))    # 0.05188680000000012
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(1_000)]', number=1000, globals=globals()))  # 0.5187156999999996
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(10_000)]', number=1000, globals=globals())) # 5.1937766


cProfile.run('array = [random.randint(1, 1_000_000) for _ in range(1000)]')
'''
5055 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<listcomp>)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
     1000    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
     1000    0.000    0.000    0.001    0.000 random.py:290(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:334(randint)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1051    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

'''

cProfile.run('array = [random.randint(1, 1_000_000) for _ in range(10_000)]')
'''
50499 function calls in 0.013 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.013    0.013 <string>:1(<listcomp>)
        1    0.000    0.000    0.013    0.013 <string>:1(<module>)
    10000    0.003    0.000    0.004    0.000 random.py:237(_randbelow_with_getrandbits)
    10000    0.004    0.000    0.008    0.000 random.py:290(randrange)
    10000    0.002    0.000    0.011    0.000 random.py:334(randint)
        1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10495    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
'''

cProfile.run('array = [random.randint(1, 1_000_000) for _ in range(100_000)]')
'''
504906 function calls in 0.128 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.020    0.020    0.127    0.127 <string>:1(<listcomp>)
        1    0.000    0.000    0.128    0.128 <string>:1(<module>)
   100000    0.029    0.000    0.043    0.000 random.py:237(_randbelow_with_getrandbits)
   100000    0.040    0.000    0.082    0.000 random.py:290(randrange)
   100000    0.025    0.000    0.107    0.000 random.py:334(randint)
        1    0.000    0.000    0.128    0.128 {built-in method builtins.exec}
   100000    0.006    0.000    0.006    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   104902    0.007    0.000    0.007    0.000 {method 'getrandbits' of '_random.Random' objects}
'''




# вариант 4 решения задачи. Через создание собственных функций max и min
def max_symbol(arr):
    max_4_ = arr[0]
    for i in arr:
        if i > max_4_:
            max_4_ = i
    return max_4_


def min_symbol(arr):
    min_4_ = arr[0]
    for i in arr:
        if i < min_4_:
            min_4_ = i
    return min_4_


max_4_ = array[0]
min_4_ = array[0]
for i in array:
    if i > max_4_:
        max_4_ = i
    elif i < max_4_ and i < min_4_:
        min_4_ = i

res_max_ = array.index(max_4_)
res_min_ = array.index(min_4_)

array[res_max_], array[res_min_] = array[res_min_], array[res_max_]
#print(f'Мой новый массив: {array}') # оставил для проверки правильности работы вариантов кода небольшой длине списка


print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(10)]', number=1000, globals=globals()))     # 0.005082199999996817
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(50)]', number=1000, globals=globals()))     # 0.024990599999998864
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(100)]', number=1000, globals=globals()))    # 0.0543446000000003
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(1_000)]', number=1000, globals=globals()))  # 0.5241085000000005
print(timeit.timeit('array = [random.randint(1, 1_000_000) for _ in range(10_000)]', number=1000, globals=globals())) # 5.163544700000003


cProfile.run('array = [random.randint(1, 1_000_000) for _ in range(1000)]')
'''
5063 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<listcomp>)
        1    0.001    0.001    0.002    0.002 <string>:1(<module>)
     1000    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
     1000    0.000    0.000    0.001    0.000 random.py:290(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:334(randint)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1059    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
'''

cProfile.run('array = [random.randint(1, 1_000_000) for _ in range(10_000)]')
'''
 50519 function calls in 0.012 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.012    0.012 <string>:1(<listcomp>)
        1    0.000    0.000    0.012    0.012 <string>:1(<module>)
    10000    0.003    0.000    0.004    0.000 random.py:237(_randbelow_with_getrandbits)
    10000    0.004    0.000    0.008    0.000 random.py:290(randrange)
    10000    0.002    0.000    0.010    0.000 random.py:334(randint)
        1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10515    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
'''

cProfile.run('array = [random.randint(1, 1_000_000) for _ in range(100_000)]')
'''
504918 function calls in 0.126 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.020    0.020    0.126    0.126 <string>:1(<listcomp>)
        1    0.000    0.000    0.126    0.126 <string>:1(<module>)
   100000    0.029    0.000    0.042    0.000 random.py:237(_randbelow_with_getrandbits)
   100000    0.040    0.000    0.082    0.000 random.py:290(randrange)
   100000    0.024    0.000    0.106    0.000 random.py:334(randint)
        1    0.000    0.000    0.126    0.126 {built-in method builtins.exec}
   100000    0.006    0.000    0.006    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   104914    0.007    0.000    0.007    0.000 {method 'getrandbits' of '_random.Random' objects}
'''


# Обший вывод
'''
1. Все 4 варината решения задач являются прямолинейными - O(n).
2. Какой код лучше (если принимать во внимание результаты timeit и cProfile в данном случае):
- по скорости выигрывает алгоритм №4 (функции макc и мин написаны самим) как в timeit
- с точки зрения плохого или хорошего кода (проверка через CProfile) также в данном случае выигрывает также вариант № 4
по скорости работы
3. по красоте кода - мне больше нравится вариант №1
4. по миминизации наптсания - варианты №2 и №3.
В общем, если судить сторго по введенным значениям, тот работа всех вариантов держиться практически на одном уровне
'''
