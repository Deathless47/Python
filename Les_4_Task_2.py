'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
'''
import timeit
import cProfile


# с помощью алгоритма «Решето Эратосфена».

# Пример с прошлых уроков (урок 2)
'''
sieve = [i for i in range(n)]
sieve[1] = 0
for i in range(2, n):
    if sieve[i] != 0:
        j = i + i
        while j < n:
            sieve[j] = 0
            j += i
res = [i for i in sieve if i != 0]
print(res)
'''

def sieve_eratosthenes(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res


def search_eratosthenes(i):
    a = sieve_eratosthenes(n)
    for number in a:
        if a.index(number) <= number - 1:
            for j in range(2, len(a)):
                if number * j in a[number:]:
                    a.remove(number * j)
        else:
            break
    return a[i - 1]

n = int(input('До какого числа просеиваем?: '))
print(sieve_eratosthenes(n))
i = int(input('Введите номер по счету простого числа: '))
print(f'Номеру {i} соответствует простое число: {search_eratosthenes(i)}')


print(timeit.timeit('sieve_eratosthenes(10)', number=1000, globals=globals()))   # 0.0023703000000003804
print(timeit.timeit('sieve_eratosthenes(50)', number=1000, globals=globals()))   # 0.007575699999999852
print(timeit.timeit('sieve_eratosthenes(100)', number=1000, globals=globals()))  # 0.014902899999999608
print(timeit.timeit('sieve_eratosthenes(500)', number=1000, globals=globals()))  # 0.06969650000000005
print(timeit.timeit('sieve_eratosthenes(1000)', number=1000, globals=globals())) # 0.1476780999999998


# без использования алгоритма «Решето Эратосфена».

def prime_number(n):
    count = 1
    number = 1
    num_prime = [2]

    if n == 1:
        return 2
    while count != n:
        number += 2
        for num in num_prime:
            if number % num == 0:
                break
        else:
            count += 1
            num_prime.append(number)
    return number
    print(number)


n = int(input('Введите натуральное число: '))
print(f'Номеру {n} соответствует простое число: {prime_number(n)}')

print(timeit.timeit('prime_number(10)', number=1000, globals=globals()))   # 0.0033716999999997554
print(timeit.timeit('prime_number(50)', number=1000, globals=globals()))   # 0.04579999999999984
print(timeit.timeit('prime_number(100)', number=1000, globals=globals()))  # 0.14927340000000022
print(timeit.timeit('prime_number(500)', number=1000, globals=globals()))  # 3.4726871
print(timeit.timeit('prime_number(1000)', number=1000, globals=globals())) # 14.197330400000002

print(150 * '*')

cProfile.run('sieve_eratosthenes(10_000)')
'''
 6 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.001    0.001    0.002    0.002 Les_4_Task_2.py:32(sieve_eratosthenes)
        1    0.000    0.000    0.000    0.000 Les_4_Task_2.py:33(<listcomp>)
        1    0.000    0.000    0.000    0.000 Les_4_Task_2.py:41(<listcomp>)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

cProfile.run('sieve_eratosthenes(100_000)')
'''
6 function calls in 0.020 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.020    0.020 <string>:1(<module>)
        1    0.016    0.016    0.019    0.019 Les_4_Task_2.py:32(sieve_eratosthenes)
        1    0.002    0.002    0.002    0.002 Les_4_Task_2.py:33(<listcomp>)
        1    0.002    0.002    0.002    0.002 Les_4_Task_2.py:41(<listcomp>)
        1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

cProfile.run('sieve_eratosthenes(1_000_000)')
'''
6 function calls in 0.271 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.006    0.006    0.271    0.271 <string>:1(<module>)
        1    0.219    0.219    0.266    0.266 Les_4_Task_2.py:32(sieve_eratosthenes)
        1    0.029    0.029    0.029    0.029 Les_4_Task_2.py:33(<listcomp>)
        1    0.018    0.018    0.018    0.018 Les_4_Task_2.py:41(<listcomp>)
        1    0.000    0.000    0.271    0.271 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''

print(150 * '*')

cProfile.run('prime_number(500)')
'''
 503 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.004    0.004    0.004    0.004 Les_4_Task_2.py:71(prime_number)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
      499    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

cProfile.run('prime_number(1_000)')
'''
1003 function calls in 0.016 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.016    0.016 <string>:1(<module>)
        1    0.016    0.016    0.016    0.016 Les_4_Task_2.py:71(prime_number)
        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

cProfile.run('prime_number(10_000)')
'''
10003 function calls in 1.500 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.500    1.500 <string>:1(<module>)
        1    1.499    1.499    1.500    1.500 Les_4_Task_2.py:71(prime_number)
        1    0.000    0.000    1.500    1.500 {built-in method builtins.exec}
     9999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''


"""
Общий вывод: алгоритм «Решето Эратосфена» в данных пример на больших значениях работает на порядки выше.
Сам код работает также лучше. Анализируя cProfiles можно сделать вывод о том, что алгоритм решения без 
«Решето Эратосфена» работает очень медленно.
"""