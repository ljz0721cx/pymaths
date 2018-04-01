# _*_ coding: UTF-8 _*_
import random

n = 1000000
k = 0

##
# 一个点落入一个边长为2的正方形中，击中内接圆的面积概率为多少
# P=pi*r*r/4=pi/4
# 求出圆周率pi=4P
#

for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        #落入圆中的次数
        k = k + 1
        #以上得出的pi=4*P
print (4 * float(k) / float(n))
