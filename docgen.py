#!/usr/bin/env python
import random

l = {
    'Вступление': ['Об этом написаны тысячи книг и сняты сотни фильмов', 'Эти вопросы всегда волновали человечество',
                   'Вопросы эти на первый взгляд кажутся простыми',
                   'Одной из самых волнующих загадок, которые всегда тревожили человечество'],
    'Обзор': ['В правильности такой точки зрения меня убеждает художественная литература',
              'Давайте вспомним произведения художественной литературы, в которых раскрывается тема',
              'Правильность своей точки зрения могу доказать, обратившись к ...',
              'Обратимся к произведениям художественной литературы',
              'За примерами давайте обратимся к произведениям художественной литературы'],
    'Постановка задачи': ['сформировать значения словаря, выполняя определённое действие',
                          'сформировать ключи словаря, выполняя определённое действие над каждым элементом',
                          'создать список словарей', ],
    'Решение задачи': ['сформировать значения словаря, выполняя определённое действие',
                       'сформировать ключи словаря, выполняя определённое действие над каждым элементом',
                       'создать список словарей', ],
    'Выводы': ['решение методом один', 'решение методом два', 'решение методом три', 'решение методом четыре',
               'решение методом пять'],
    'Заключение': ['заключение 1', 'заключение 2', 'заключение 3', 'заключение 4']}
for k in sorted(l.keys()):
    print(k, random.choice(l[k]))