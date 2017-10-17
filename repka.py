#!/usr/bin/env python

def repka():
    members = ['Дедка', 'Бабка', 'Внучка', 'Жучка', 'Мышка']
    skazka = members[0] + 'за репку\n Тянет-потянет, вытянуть не может.\n'
    for i in range(len(members)):
        try:
            skazka += members[i+1] + ' за ' + members[i] + ', ' + members[i] + ' за репку\n' + \
                'Тянут-потянут, вытянуть не могут.\n'
        except Exception as err:
            print(err)
    return skazka

print(repka())

