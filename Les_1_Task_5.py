"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв.
"""

letter = 'abcdefghijklmnopqrstuvwxyz'
let_1 = input('Введите букву №1: ')
let_2 = input('Введите букву №2: ')
print(f'Буква: - ' f"{let_1} стоит под номером {letter.index(let_1)}")
print(f'Буква: - ' f"{let_2} стоит под номером {letter.index(let_2)}")
if letter.index(let_2) > letter.index(let_1): # УСЛОВИЕ 1 В ДИАГРАММЕ
    print(f'Между буквами находятся букв: {(letter.index(let_2) - letter.index(let_1)) - 1}')
elif letter.index(let_2) == letter.index(let_1): # УСЛОВИЕ 2 В ДИАГРАММЕ
    print('расстояние между буквами отсутствует, так как вы задали одинаковые буквы')
else: # УСЛОВИЕ 3 В ДИАГРАММЕ
    print(f'Между буквами находятся букв: {(letter.index(let_1) - letter.index(let_2)) - 1}')
# -1 добавляем так как индекс начинается с 0