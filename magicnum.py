#!/usr/bin/env python

import random
count = 0
def main():
    magicd = random.randint(1,100)
    while True:
        try:
            global count
            d = int(input('Угадай число от 1 до 100: '))
            if d == magicd:
                print('Ты угадал!!!')
                count += 1
                break
            elif d > 100 or d < 1:
                print('1-100')
                continue
            elif d < 100 and d > magicd:
                print('Чуть меньше')
                count += 1
                continue
            elif d > 1 and d < magicd:
                print('Чуть больше')
                count += 1
                continue
        except Exception as err:
            print(err)


if __name__ == '__main__':
    main()
    print('Попыток: ', count)
