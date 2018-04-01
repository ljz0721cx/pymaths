# coding=utf-8
# __authon__="lijianzhen"

'''
python 变量存储在内存中，在内存中开辟空间
基于变量的数据类型，解释器会分配指定内存，决定什么数据被存储在内存中
变量可以指定不同的数据类型，可以是整数，小数或字符

1.python变量不需要类型声明
2.每个变量在内存中创建，都包括变量的标识，名称和数据这些信息
3.每个变量在使用前必须赋值，变量赋值以后才会被创建
'''
# 单个变量赋值
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点数
name = "Janle"  # 字符串
print counter,
print miles,
print name

# 多个变量赋值
# 三个变量被分配到相同的内存空间上
a = b = c = 1
# 多个对象指定多个变量。
x, y, z = 1, 2, "janle"
print a,
print x,
print y,
print z;

# python数字
# 数字类型用于存储数值，是不可改变的数据类型，这意味着数字的数据类型会分配一个新的对象
num1 = 1
num2 = 10
# del num1 #删除对应的引用
print num1
# python支持4中不同的数字类型 int long float complex

# Python字符串
s = "iloveyou"
print s[1:5],
print s[5:],
print s * 2
print s + "sure"

# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数的集合类数据实现，它支持字符串，数字，字符和嵌套集合
list = ["Janle", 88, 80, "lijian", 30.09]
list1 = ["repeat", "end"]
print list
print list[0]
print list[1:3]
print list[2:]
print list1 * 2
print list + list1
print "==========================tuple================"
# python 元组
# 元组是另外一个数据类型，类似于list，元组用（）标识,内部元素用逗号隔开，但是元组不能二次赋值，相当于只读列表
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print tuple  # 输出完整元组
print tuple[0]  # 输出元组的第一个元素
print tuple[1:3]  # 输出第二个至第三个的元素
print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2  # 输出元组两次
print tuple + tinytuple  # 打印组合的元组

list[2] = 1000
print list
# object does not support item assignment
# tuple[2] = 1000    # 元组中是非法应用
print tuple

# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型
print "===========================dictionary======"
# 字典是无序的对象集合，列表是有序的对象集合，字典通过key来存取，不是通过偏移量来存储和map类似
dict = {}
dict[1] = "first"
dict["2"] = "secend"
tinydict = {"3": "third", "4": "four"}

print dict[1]
print dict["2"]  #这里存入什么就是什么，不要存入整型，用字符串取
print tinydict
print tinydict.keys()
print tinydict.values()

#Python数据类型转换
print "===========================数据类型的转换======"
#数据类型的转换，只需要将数据类型作为函数名即可。
print int("2")

'''
isinstance 和 type 的区别在于：
class A:
    pass

class B(A):
    pass

isinstance(A(), A)  # returns True
type(A()) == A      # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False
区别就是:
 type()不会认为子类是一种父类类型。
 isinstance()会认为子类是一种父类类型。
'''