name = "boy"
print(name)
a = "victor"
b = "is"
c = "best"
k =5.00
print(a,b,c)
x, y, z = "Orange", "Banana", "Cherry"
print (x, y, z)
boy = "good"
def add():
    print("python is " + boy)
add()
def greeting():
    print("good morning! " + a)
greeting()
print(type(x))
print(type(k))
#convert variables
n = complex(k)
print(n)
#random fun
import random
print(random.randrange(0, 100))
de = "hello world"
print(de[3:])
print(de.upper())
print(de.replace("hello", "love"))
age = 23
txt = "I am \"Victor\", and \ni am {} years old"
print(txt.format(age))
print(8>9)
A = 200
B = 45
A%=B
if B>A:
    print("B is greater than A")
else:
    print("B is lessthan A")
    print(A)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.remove("melon")
print(thislist)
for x in thislist:
    print(x)
if "apple" in thislist:
    print("yes apple is in the list")
print(thislist[4])
print(thislist[1:6])
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
new =[]
for t in fruits:
    if "a" in t:
        new.append(t)
        print(new)
        print(len(new))
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
for i in range (len(thistuple)):
    print(thistuple[i])