#!/usr/bin/env python

from random import randint, choice

info = ''' >>> МОРСКОЙ БОЙ <<<
Параметры игрового поля:
 0 - пустая ячейка
 1 - занята кораблем
 -1 - подбит
'''
v = 'abcdefghij'
userboard = [[0 for x in range(10)] for y in range(10)]
pcboard = [[0 for x in range(10)] for y in range(10)]

def FreeDot(board, x, y):
    if board[x][y] == 0:
        return True
    else:
        return False

def ErrorDot(x, y):
    if x in v and 0 > int(y) < 11:
        return True
    else:
        return False

def PrintBoard(board):
    print('   ', end='')
    for i in range(1, 11):
        print(i, end='  ')
    print()
    for i in range(len(board)):
        print('{} {}'.format(v[i], board[i]))

def UserInputShips():
    InputShip4()

def InputShip4():
    s, e = input('Введите координаты четырехтрубника (например b3-b6): ').split('-')
    if s[0] == e[0]:
        for i in range(int(s[1])-1, int(e[1])):
            userboard[v.index(s[0])][i] = 1
    elif int(s[1]) == int(e[1]) and s[0] != e[0]:
        for i in range(v.index(s[0]), v.index(e[0])+1):
            userboard[i][int(s[1])] = 1

def InputShip3():
    s, e = input('Введите координаты трехтрубника (например с2-e2): ').split('-')
    if s[0] == e[0]:
        for i in range(int(s[1])-1, int(e[1])):
            userboard[v.index(s[0])][i] = 1
    elif int(s[1]) == int(e[1]) and s[0] != e[0]:
        for i in range(v.index(s[0]), v.index(e[0])+1):
            userboard[i][int(s[1])] = 1


if __name__ == '__main__':
    print(info)
    UserInputShips()
    PrintBoard(userboard)
