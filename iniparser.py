#!/usr/bin/env python
cfg = {}
seccount = 0
varcount = 0
with open('config.ini', 'r') as f:
	for s in f:
		if s.startswith('['):
			seccount += 1
			kk = s.strip('[[]]\n')
			cfg[kk] = {}
		else:
			varcount += 1
			k, v = s.split('=')
			cfg[kk][k] = v.rstrip('\n')

print(cfg)
print('Секций = {0}, Переменных = {1}'.format(seccount, varcount))