# _*_ coding: UTF-8 _*_
import random

'''
设计3个对象：汽车，游戏，蒙提霍尔
'''


class Car(object):
    def init(self):
        self.mPosition = random.randint(1, 3)


class Gamer(object):
    def init(self):
        self.mSelect = random.randint(1, 3)

    def doChange(self):
        door = [1, 2, 3]
        door.pop(list.index(door, self.mSelect))
        door.pop(list.index(door, montyhall.mOpeningDoor))
        self.mSelect = door[0]


class MontyHall(object):
    def init(self):
        self.mCarPosition = car.mPosition
        self.mGamerSelect = gamer.mSelect

    def openDoor(self):
        door = [1, 2, 3]
        if self.mCarPosition == self.mGamerSelect:
            door.pop(list.index(door, self.mCarPosition))
            self.mOpeningDoor = door[random.randint(0, 1)]
        else:
            door.pop(list.index(door, self.mCarPosition))
            door.pop(list.index(door, self.mGamerSelect))
            self.mOpeningDoor = door[0]


if __name__ == '__main__':
    car = Car();
    gamer = Gamer();
    montyhall = MontyHall()
    win = [0, 0, 0]
    for p in range(3):
        for k in range(10000):
            car.init()
            gamer.init()
            montyhall.init()
            montyhall.openDoor()
            if p == 0:
                if random.randint(0, 1) == 1:
                    gamer.doChange()
            elif p == 1:
                pass
            else:
                gamer.doChange()
            if gamer.mSelect == car.mPosition:
                win[p] = 1
    print('不确定是否改变选择的概率为：%s' % (float(win[0]) / 10000))
    print('确定不改变选择的概率为：%s' % (float(win[1]) / 10000))
    print('确定改变选择的概率为：%s' % (float(win[2]) / 10000))
