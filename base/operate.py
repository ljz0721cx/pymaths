# coding=utf-8
# __authon__="lijianzhen"

# python算术运算符
a = 21
b = 10
c = 0
c = a + b
print "a+b的值为：", c
c = a - b
print "a -b 的值为", c
c = a * b
print "a * b 的值为：", c
c = a / b
print "a / b 的值为：", c
c = a % b
print "a % b 的值为：", c
c = a ** b
print "a ** b 的值为", c

# 比较运算符
print a == b

if a >= b:
    print "a >= b"
else:
    print "a < b"

# 赋值运算符
c += a
print "c += a", c
c -= a
print "c -= a", c
c *= a
print "c *= a", c
c /= a
print "c /= a", c  # 除法赋值运算符
c = 21
c %= a
print  "c %=a：", c
c = 21
c **= a
print "c **= a：", c
c = 21
c //= a
print "c //= a：", c  # 取整除

# 位运算符
w = 60  # 0011 1100
y = 13  # 0000 1101
# ----------------------
print "w:", w
print "y:", y
print "w&y:", w & y
print "w|y:", w | y
print "w^y:", w ^ y
print "~w:", ~w
print "w << 2:", w << 2
print "w >> 2:", w >> 2

# 逻辑运算符
a = 0
b = 20
if (a and b):
    print "a and b的变量都为true"
else:
    print "a and b的变量不都为true"

if (a or b):
    print "a and b的变量都为true"
else:
    print "a and b的变量不都为true"

if not (a or b):
    print "a and b的变量都为true"
else:
    print "a and b的变量不都为true"

# 成员运算符
list = [1, 2, 3, 4, 5, 6];
l = 3
x = 19
if (l in list):
    print "变量l=3在list中"
else:
    print "变量l=3不在list中"

if (x not in list):
    print "变量x=19不在list中"
else:
    print "变量x=19在list中"

y = list[:] #将list数组的引用地址赋值给y
print "y == list", y == list
print "y is list", y is list

# 身份运算符
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
wo = 10
you = 10
if (wo is you):
    print "我就是你"
else:
    print "我不是你"

if (wo is not you):
    print "我不是你"
else:
    print "我就是你"


'''
以下表格列出了从最高到最低优先级的所有运算符：
**	  指数 (最高优先级)
~ + -	  按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	   乘，除，取模和取整除
+ -   	加法减法
>> <<	   右移，左移运算符
&	   位 'AND'
^ |     位运算符
<= < > >=	  比较运算符
<> == !=	  等于运算符
= %= /= //= -= += *= **=	      赋值运算符
is is not	    身份运算符
in not in	    成员运算符
not or and	     逻辑运算符
'''