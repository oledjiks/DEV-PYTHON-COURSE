#!/usr/bin/env python

import shelve
import datetime
from optparse import OptionParser

def main():
    db = shelve.open("reminerdb")
    parser = OptionParser(description='Программа "Напоминалка"')
    parser.add_option("-l", "--lst", action="store_true", help="Вывод всех собитый")
    parser.add_option("-a", "--add", dest="newevent", nargs=2,
        help='Добавить новое событие (пример: reminder.py -a 2017-09-10 "Сходить на лекцию по Python")')
    parser.add_option("-e", "--evrange", dest="evrange", nargs=2,
        help="Вывод событий по заданному интервалу времени (пример: reminder.py -e 2017-09-01 2017-09-30)")
    (options, args) = parser.parse_args()
    if options.lst:
        for k, v in db.items():
            print('Дата: {}  Событие: {}'.format(k, v))
    elif options.newevent:
        data = ' '.join(options.newevent[1:])
        print('Добавлено новое событие')
        db[options.newevent[0]] = str(data)
    elif options.evrange:
        y, m, d = tuple([int(i) for i in options.evrange[0].split('-')])
        dbegin = datetime.date(y, m, d)
        y, m, d = tuple([int(i) for i in options.evrange[1].split('-')])
        dend = datetime.date(y, m, d)
        for k, v in db.items():
            y, m, d = tuple([int(i) for i in k.split('-')])
            kk = datetime.date(y, m, d)
            if kk >= dbegin and kk <= dend:
                print('Дата: {}  Событие: {}'.format(k, v))
    db.close()

if __name__ == '__main__':
    main()