# -*- coding: utf-8 -*-

"""
1, 变量赋值
2, 基本的数据类型（整数，浮点数，字符串，布尔值，None），数据结构(列表，字典)
3, 判断，条件语句
4, 循环语句
5, 函数使用

写程序的时候，需要注意的是 中文符号 不行，例如 () 和 （） 这是有区别的
变量是我们用来保存（引用） python 中定义好的数据，这样我们就可以在需要的时候随时拿到它
变量赋值，变量是用人能够看懂的名词指向一个在某语言中具体的数据类型
a = 1
不能用数字作为变量名的开头
那为什么要有变量呢，主要是为了程序的可读性，以及数据的复用
比如画一个正方形，边长为 90，那么可以 side_length = 90
需要用这个数的时候，直接拿变量就好，语义也清晰，而且，当要改变边长的时候，只要修改一处，即可

int 整数 1 2 3
float 浮点数 1.2 1.0 3.1
整数浮点数之间可以直接比较
str 字符串 "abc" 'abc' 二者等价
bool 布尔值 True False 只有两个，注意大写
None 特殊的值，判断一个变量值是否为 None，可以用 a is None 或者 a == None，推荐 前者
list [] 有序的数据列表，['cat', 'dog', 'rabbit', 1, 1.2, None, True]  可以放 任意数据类型
dict {} 字典，通过 key 来取 value，{"cat": "harper", "dog": "qq"}

if condition:
    ...  # 执行体
else:
    ...  # 前者 condition 不为 True 的时候， 将会执行的部分

loop
while condition:
    ...

loop
for i in container:
    ...

function
这是最重要的概念，作为功能的抽象
def do_something(params):
    ...  # 将专做一类事情的操作集中在这里
"""

# 这个符号代表注释，也就是说只给人看，机器（电脑）会直接跳过

a = 1
b = 2
# 变量之间可以相互传递
# 变量的赋值相当于是一种引用，比如 2 这个 int，存在电脑内存中的某一个位置，你有一个变量池，可以定义任一个变量名，b 引用了 2， c 也引用了 2
c = b
# print 的作用在于让我们清晰的看到程序执行的时候，某些变量的值到底是多少，注意，这是个函数
print(a, b, c)
# 改变 b 的值，并不会影响 c 原先的值
b = 3
print(c)

d = a + b
# 整数 和 浮点数之间可以相加，不会局限于自身
print(d)
# 比较符号 < > == >= <=
# 有这样的 符号，执行后返回的肯定是 bool 值
e = a < b
print(e)

# 字符串可以是 双引号 和单引号
name = "pengpeng"
full_name = 'peng guan hua'
print(name)
print(full_name)

# list 有序的数组
house = ['playstation', 'guitar', {"cat": "harper", "laptop": "mac", "space_size": 10, }]  # 逗号 , 可加 可不加，但是为了一致性，我们加上
# 通过下标取值，从 0 开始
print(house[0])
print(house[1])
print(house[2])
# 超出的话，将会 报错，即程序不会再执行
# print(house[3])


# dict 通过 key 获取 value 的数据结构，一般这么写，为了可读性
sample = {
    "cat": "harper",
    "laptop": "mac",
    "space_size": 10,
}
# 通过 key 取值， 两种方式 [] 和 .get()
print(sample["cat"])
print(sample.get("cat"))
# 没有指定 key 的时候, [] 取法会报错，.get() 会返回 None
# print(sample["dog"])
print(sample.get('dog'))

cat = sample['cat']
# 条件结构体，当条件满足的时候，只会执行其中的一条，else 也可以不写
if cat == "harper":
    print('喵~~~')
elif cat == "luna":  # 这是进一步的条件判断
    print('水兵月')
else:
    print('汪!!!')

dog = sample.get("dog")
if dog is not None:
    print('汪!!!')
print('whatever dog exists')

# loop 循环结构
limit = 5
i = 0
while i < limit:
    if i == 3:
        i += 1
        # continue 跳过当下，即后续的代码不执行，重新进行 condition 判断
        continue
    if i == 4:
        print('i\'ve got 4,that\'s enough')
        break
    print(i)
    # 循环必须保持有穷性，即 一定会结束，不然没有意义
    i += 1

loop_container = ['a', 'b', 'cc', 'dd', 12, 1.5]
# for ... in ... 这样的语句可以遍历一个 list，逐个获取里面的元素
for item in loop_container:
    print(item)


# 函数定义
def average(data_list):
    # 假设输入的参数是一个 list
    data_length = len(data_list)
    data_sum = 0
    for data in data_list:
        data_sum += data
    # return 的值是给调用函数方来使用的，当然，函数也可以不规定返回，默认的就是 None，比如 print 函数，只是做某一件事情
    return data_sum / data_length


print(average([1, 2, 3, 4, 10, 10, 10, 6]))