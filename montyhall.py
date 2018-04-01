# coding=utf-8
# __authon__="lijianzhen"
# 主要是蒙提霍尔问题
import random


def MontyHall(Dselect, Dchange):
    Dcar = random.randint(1, 3)
    if Dcar == Dselect and Dchange == 0:  # 一开始选中而不改变选择
        return 1
    elif Dcar != Dselect and Dchange == 0:  # 一开始没选中而且不改变选择
        return 0
    elif Dcar == Dselect and Dchange == 1:  # 一开始选中而且改变选择
        return 0
    else:
        return 1  # 一开始没有选中而且改变选择


n = 10000
win = 0
##
# 不确定改变选择
for i in range(n):
    Dselect = random.randint(1, 3)
    Dchange = random.randint(0, 1)
    win = win + MontyHall(Dselect, Dchange)
print(float(win) / float(n))

##
# 确定是不改变选择
win = 0
for i in range(n):
    Dselect = random.randint(1, 3)
    Dchange = 0
    win = win + MontyHall(Dselect, Dchange)
print(float(win) / float(n))

##
# 确定改变选择
win = 0
for i in range(n):
    Dselect=random.randint(1,3)
    Dchange=1;
    win=win+MontyHall(Dselect,Dchange)
print(float(win)/float(n))
