#!/usr/bin/python3
# -*- coding: UTF-8 -*-
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
# print(bicycles[4]) # IndexError: list index out of range
print(bicycles[-1])
bicycles.append("nico")
print(bicycles)
# bicycles.clear()
# print(bicycles)
print(bicycles[-2])

# modify
bicycles[-1]='ruirui'
print(bicycles)
# insert
bicycles.insert(0,"ruirui")
bicycles.insert(1,"tiantian")
print(bicycles)
bicycles.remove('ruirui')
ruirui=bicycles.pop()
print(bicycles)
print(ruirui)

# delete item
del bicycles[1]
del bicycles[-1]
print(bicycles)

# pop

print(bicycles.count("ruirui"))

print("你好 世界")
# sort 永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
# sorted 临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)

# reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
# length
print(len(cars))
print(cars[-1])
