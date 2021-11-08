'''
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
'''

#board = [['_'] * 3 for _ in range(253)]
#print(board)

board = []

for i in range(5):
    board.append([])
    summa = 0
    for j in range(3):
        number = int(input(f'Введите цифру {i+1} и {j+1} столбца: '))
        summa += number
        board[i].append(number)
    board[i].append(summa)

for n in board:
    print(('{:>5d} ' * 4).format(*n))