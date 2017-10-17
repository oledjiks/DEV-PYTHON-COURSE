#!/usr/bin/env python

''' Параметры доски:
0 - пустая ячейка
1 - занята кораблем
-1 - подбита
'''

from random import randint, choice

userboard = [[0 for x in range(10)] for y in range(10)]
pcboard = [[0 for x in range(10)] for y in range(10)]


def CheckFreePos(x, y, board):
    if board[x][y] == 0:
        return True
    elif board[x][y] == 1:
        return False


def PrintBoard(board):
    for i in board:
        print(i)


def UserShipsInit():
    global userboard

def GameInit():
    print('>>> Игра Морской бой <<<')
    UserShipsInit()

if __name__ == '__main__':
    GameInit()
