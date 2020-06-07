# coding:utf-8
import keyword

import math

"""from selenium import webdriver

path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://www.baidu.com")
driver.maximize_window()  # 好像没有效果。。。"""

# print(keyword.kwlist)
# print(round(1/3,6))
# print(type(3.1415926))
# welcome = '你好，欢迎到松勤自动化班级学习。好好学习'
# print('小张 '+welcome)
# print('小李 '+welcome)
#
# print(id(welcome))#查看一个对象的内存地址
# print(math.modf(3.25))
# print(math.modf(4.2))
# print(math.modf(3.1324))

# info = 'name  is \r tom'
# print(info)
# str = 'abcdefg'
# print(str[len(str)-3])
#
# print(str[-len(str)])
#
# print(str.index('c'))
#
# print(str[1:1+3:1])
# print(str[1:1+5:1])
# print(str[1:1+3:2])
alist = [10, 3.14, 'hello', [100, 200]]
# print(type(alist))
# print(len(alist))
# print(alist[3])
# print(100 in alist[-1])
# print(alist[:2])
# print(alist[1:3])
# print(alist[3])
# alist[0] = 20
# print(alist)
# alist.append(40)
# alist[-2].append(300)
# alist.insert(0,500)

# alist = [10,20,30,40,20,50,20]
# del alist[1],alist[2]
# del alist[1:1+2]
# del alist[::2]
# print(alist)
# res = alist.pop(1)
# print(res)
# when 20 in alist:alist.remove(20)

# alist = [10,20,30]
# print(alist+[40,50])#另存新地址
# print(alist)
# alist.extend([70,80])#扩展--原地址。
# print(alist)

# print(3!=1)
# print('abc' > 'ab')
# print('a,c' in 'abcd')
# print('1,3'in '1,3,5')
#
# alist = [10,20,30]
# print(10,20 in alist)


# def func():
#     print('-----函数运行了-----')
#     return True
#
# #print(func())
#
# if 3 == 1 and func():
#     print('我执行了！
#
# alist = [10,20,[100,200]]
# blist = alist
# blist.append(30)
# print('alist: ',alist,' ; id是: ',id(alist))
# print('blist: ',blist,' ; id是: ',id(blist))

import copy

# alist = [10,20,[100,200]]
# blist = copy.copy(alist)#复制
# # blist.append(30)
# blist[-1].append(300)
# print('alist: ',alist,' ; id是: ',id(alist))
# print('blist: ',blist,' ; id是: ',id(blist))

# alist = [10,20,[100,200]]
# blist = copy.deepcopy(alist)
# # blist.append(30)
# blist[-1].append(300)
# blist.append(30)
# print('alist: ',alist,' ; id是: ',id(alist))
# print('blist: ',blist,' ; id是: ',id(blist))


# a = '-1000'
# b = int(a)
# print(b,type(b))
# print(a,type(a))
#
# str = 'abssderfgaEEfSdqa'
# print(str.count('a'))
# print(str.startswith('D'))
# print(str.endswith('a'))
# print(str.find('s'))
# print(str.find('G'))

# alist = ['i','like', 'football']
# print("*".join(alist))

# lists = {"m",1000,"m2",2000}
# for a in lists:
#     print(a)

# for item in lists:
#     item = 0;
# print(lists)

lists = ["m1", 1900, "m2", 2000]

# count = 0
#
# while count < len(lists):
#     print(lists[count])
#     count = count + 1


# for index in range(len(lists)):
#     print(lists[index])


# for val in iter(lists):
#     print(val)

# for i,val in enumerate(lists,2):
#     print(i,val)
# returnNums = []
# nums = [int(t) for t in input("请输入一组整数数组，以空格分开：").split()]
# target = int(input("请输入目标值:"))
# for i in nums:
# 	nums_index = nums.index(i)
# 	for t in nums[nums_index+1:]:
# 		if t + i == target and len(returnNums) != 2:
# 			returnNums.append(nums.index(i))
# 			returnNums.append(nums[nums_index+1:].index(t) + (nums_index+1))
# print("返回值：",returnNums)


"""如果列表有奇数个整数，则输出中间那个
如果列表有偶数个整数，则输出中间两个的平均值"""

# L = [int(t) for t in input("请输入一组数字，以空格分开").split()]
#
#
# l = len(L)
# L.sort()  #列表生序排列
# if l%2 == 0:
#     m = (L[int(l/2)-1]+L[int(l/2)]) /2
#     print("%.1f" % m)
# else:
#     m = L[int((l - 1) / 2)]
#     print(m)

# 求两数相加 等于 目标数值 的函数
# L = [int(t) for t in input('数字 + 空格').split()]
# target = int(input("请输入目标值："))
# m = []
# for i in range(len(L)-1):
#     for j in range(i+1,len(L)):
#         if L[i] + L[j] == target :
#             m.append(L[i])
#             m.append(L[j])
# print(m)


# A = [33, 55, 66, 22, 34, 24, 54, 44]
# count = 0
# for i in range(len(A)):
#     for j in range(len(A) - 1):
#         if A[i] + A[j] == 98:
#             count = count + 1
#
# print(count)
