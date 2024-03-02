import math
import datetime


def pow(a, n):
    if n == 1:
        return a
    return a * pow(a, n-1)


#print(pow(2,5))


def count(n):
    if n < 10:
        return 1
    return 1 + count(n//10)

#print(count(0))


def fibo(n):
    if n < 3:
        return 1
    return fibo(n-1) + fibo(n-2)


#d = datetime.datetime.now()
#print(fibo(20))
'''f1 = 1
f2 = 1
# Fn = F(n-2) + F(n-1)
n = 20
k = 2
while k < n:
    fn = f1 + f2
    f1 = f2
    f2 = fn
    k += 1
print(fn)'''
#print(datetime.datetime.now()-d)



#==================================================

import random
import os
boardSize = 3
board = [[' ' for i in range(boardSize)] for j in range(boardSize)]

def printBoard(board):
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("--+---+--")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("--+---+--")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    print()
    print()

def choiceComp(board):
    while(True):
        n = random.randint(1, 9)
        if board[(n-1)//3][(n-1)%3] == ' ':
            return n


def isWinner(board):
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != ' ': # 1 2 3
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] and board[1][0] != ' ': # 4 5 6
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] and board[2][0] != ' ': # 7 8 9
        return board[2][0]
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != ' ': # 1 4 7
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != ' ': # 2 5 8
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != ' ': # 3 6 9
        return board[0][2]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ': # 1 5 9
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ': # 3 5 7
        return board[0][2]
    return ' '

def move(board, n, symbol):
    board[(n - 1) // 3][(n - 1) % 3] = symbol
    printBoard(board)



count = 0
winner = ' '
while(winner == ' '):
    move(board, int(input("N : ")), 'X')
    count += 1
    winner = isWinner(board)
    if(winner != ' '):
        print(f"Перемога {winner}")
        break
    move(board, choiceComp(board), '0')
    count += 1
    winner = isWinner(board)
    if (winner != ' '):
        print(f"Перемога {winner}")
        break



# X | X | X
# --+---+--
# X | X | X
# --+---+--
# X | X | X


