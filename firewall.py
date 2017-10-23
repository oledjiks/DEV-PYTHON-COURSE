#!/usr/bin/env python
import random, socket, struct

def ip2int(addr):
	return struct.unpack("!I", socket.inet_aton(addr))[0]

"""
словарь для правил фильтрации
{1: ['permit|deny', 'srcaddr', 'srcmask', 'dstaddr', 'dstmask']}
"""

rules = {}

def addrule(rulestr):
    try:
        num = random.randint(0, 1000)
        rules[num] = rulestr.split()
    except SyntaxError as err:
        print '%s' % err

def listrule():
    for k, v in rules.items():
        print k, ' '.join(v)
    
def delrule(num):
    if num in rules:
        del rules[num]

def filterrule(srcadr, dstadr):
    for k, i in rules.items():
        src = ip2int(srcadr)
        dst = ip2int(dstadr)
        if i[0] == 'permit' and ip2int(i[1]) == src and ip2int(i[3]) == dst:
            return True
        elif i[0] == 'deny' and ip2int(i[1]) == src and ip2int(i[3]) == dst:
            return False
        else:
            print 'Нет таких адресов в таблице фильтрации пакетов'


