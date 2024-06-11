# name = "boy"
# print(name)
# a = "victor"
# b = "is"
# c = "best"
# k =5.00
# print(a,b,c)
# x, y, z = "Orange", "Banana", "Cherry"
# print (x, y, z)
# boy = "good"
# def add():
#     print("python is " + boy)
# add()
# def greeting():
#     print("good morning! " + a)
# greeting()
# print(type(x))
# print(type(k))
# #convert variables
# n = complex(k)
# print(n)
# #random fun
# import random
# print(random.randrange(0, 100))
# de = "hello world"
# print(de[3:])
# print(de.upper())
# print(de.replace("hello", "love"))
# age = 23
# txt = "I am \"Victor\", and \ni am {} years old"
# print(txt.format(age))
# print(8>9)
# A = 200
# B = 45
# A%=B
# if B>A:
#     print("B is greater than A")
# else:
#     print("B is lessthan A")
#     print(A)
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist.remove("melon")
# print(thislist)
# for x in thislist:
#     print(x)
# if "apple" in thislist:
#     print("yes apple is in the list")
# print(thislist[4])
# print(thislist[1:6])
# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# new =[]
# for t in fruits:
#     if "a" in t:
#         new.append(t)
#         print(new)
#         print(len(new))
# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i = i + 1
# for i in range (len(thistuple)):
#     print(thistuple[i])
# dic = {
#     "brand": "HP",
#     "version": "Windows 11",
#     "price": "1000USD"
# }
# dic["brand"] = "Dell"
# print(dic)
# print(dic["brand"])
# print(len(dic))
# print(type(dic))
# print(dic)
# dic["color"] = "silver"
# print(dic)
# for x, y in dic.items():
#     print(x, y)
# a = 45
# b = 45
# if a > b:
#     print("a is greater than b")
# elif b==a:
#     print("b is equal to a")
# else:
#     print("b  greater than a ")
# i = 0
# g = "the number is {}"
# while i < 90:
#     print(g.format(i))
#     i = i + 1
# for i in range(6):
#     print(i)
# name = "victor"
# hi = 60
# you = "Good morning {} "
# def greet():
#     print(you.format(hi) + name)
# greet()
# x = lambda a,b: a*b
# print(x(5,9))
# no = "the number is {}"
# li = ["bool", "hen", "ken"]
# li[0] = "cow"
# print(li)
# for g in range (10):
#     print(no.format(g))
# g = lambda a: a + 10
# print(g(20))
# class vic:
#     x =6
# print(vic)
# class person:
#     def __init__(self, name, age):
#         self:name = name
#         self:age = age
# ty = person("BOSCO", 45)
# print(ty.name)
# print(ty.age)
# import random
# print(random.randrange(45,100))
# mymodule = {
#      "name": "John",
#      "age": 36,
#      "country": "Norway"
# }
# import platform
# x = dir(platform)
# print(x)
# import datetime
# h = datetime.datetime.now()
# print(h.year)
# print(h.strftime("%w"))
# print(h.strftime("%H"))
# import math
# x = math.sqrt(36)
# y = math.cos(180)
# print(y)
# print(x)
# import json
# x = { "name":"John", "age":30, "city":"New York"}
# y = json.dumps(x)
# print(y)
# import re
# f ="nuwagaba@gmail.com"
# l = re.findall("@", f)
# print(l)
f=open("C:\\plp\demo.txt", "r")
for i in f:
    print(i)
g = open("demo.txt", "a")
g.write("be close to people")
g.close()
g = open("demo.txt", "r")
print(g.read())
a = 67
g = 87
print(a+g)
