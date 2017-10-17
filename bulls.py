#!/usr/bin/env python
import random

digits = [x for x in range(10)]
random.shuffle(digits)
conceived = digits[:4]
if conceived[0] == 0:
    conceived[0] = conceived[1]
    conceived[1] = 0
print('Игра "Быки и Коровы"')
while True:
    guessed = int(input("Введите число: "))
    if not 999 < guessed < 10000:
        print("Число от 1000 до 9999")
        print("Число от 1000 до 9999")
        continue
    testing = [int(x) for x in str(guessed)]
    if testing == conceived:
        print("Вы выиграли!")
        print("Это было", conceived)
        break
    for n, d in enumerate(testing):
        if d == conceived[n]:
            print("Б", end="")
        elif d in conceived:
            print("К", end="")
        else:
            print(d, end="")
    print()
