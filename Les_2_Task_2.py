'''
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

num = input('Введите целое число: ')
even = 0
odd = 0
for _ in num:
    i = int(_)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'Четных чисел: {even}\n'
      f'Нечетных чисел: {odd}')


