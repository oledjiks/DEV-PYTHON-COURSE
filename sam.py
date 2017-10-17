#!/usr/bin/env python

class SamCreator:

    Sg = 1
    Dr = 0.1
    G = 0.2
    W = 3

    def __init__(self, sam):
        self.sam = sam

    def load_sugar(self):
        print('берем {} кг сахара'.format(round((self.Sg * self.sam), 1)))

    def load_barm(self):
        print('берем {} кг дрожжей'.format(round((self.Dr * self.sam), 1)))

    def load_pease(self):
        print('берем {} кг гороха'.format(round((self.G * self.sam),1)))

    def load_water(self):
        print('берем {} литров воды'.format(self.W * self.sam))

    def working(self):
        print('Для {} литров крутейшего самогона надо - '.format(self.sam))
        self.load_sugar()
        self.load_barm()
        self.load_pease()
        self.load_water()
try:
    litres = int(input('Введите количество литров: '))
    sam = SamCreator(litres)
    sam.working()
except ValueError as err:
    print('необходимо ввести число')


