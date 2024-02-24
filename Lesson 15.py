#Напишіть функцію, що перевертає вміст списку цілих.

import random

'''n = int(input("n = "))
list1 = [random.randint(0, 10) for i in range(n)]
print(list1)'''

def reverseList(_list):
    for i in range(len(_list) // 2):
        _list[i], _list[len(_list) - 1 - i] = _list[len(_list) - 1 - i], _list[i]


#reverseList(list1)
#print(list1)

# Напишіть функцію, що обчислює факторіал кожного елемента списку цілих. Функція повертає новий список, який містить отримані факторіали.

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def listFactorials(_list):
    '''factL = []
    for elem in _list:
        factL.append(factorial(elem))
    return factL'''
    return [factorial(i) for i in _list]

#fl = listFactorials(list1)
#fl = [factorial(i) for i in list1]
#print(fl)


# Описать процедуру Chessboard(R, C), формирующую по целым
# положительным числам R и C матрицу A размера R × C, которая содержит
# числа 0 и 1, расположенные в «шахматном» порядке, причем A[0,0] = 0. Дву-
# мерный целочисленный массив A является выходным параметром. С по-
# мощью этой процедуры по данным целым числам R и C сформировать
# матрицу A размера R × C.

def Chessboard(row, col):
    board = []
    for i in range(row):
        boardRow = []
        if i % 2 == 0:
            boardRow = [j % 2 for j in range(col)]
        else:
            boardRow = [(j + 1) % 2 for j in range(col)]
        board.append(boardRow)
    return board

b = Chessboard(8,8)
def printBoard(board):
    for r in board:
        print(r)

#printBoard(b)


def fact_r(n):
    if n == 1:
        return 1
    return n * fact_r(n-1)

print(factorial(5))
print(fact_r(5))


def number(n):
    print(n, end=' ')
    if n > 1:
        number(n-1)

number(5)
print()

def num(n):
    if n > 1:
        num(n-1)
    print(n, end=' ')

num(5)

def summab(a, b):
    if a == b:
        return a
    return a + summab(a + 1, b)

print(summab(1,10))