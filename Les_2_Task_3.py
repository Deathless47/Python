'''
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
'''
number = int(input('Введите число: '))
result = 0
while number > 0:
    result = result * 10 + number % 10 # 10 - количество всех цифр от 0 до 10
    number = number // 10
print(result)