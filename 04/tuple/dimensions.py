# Python将不能修改的值称为不可变的 ，而不可变的列表被称为元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0]=1 # 报错 'tuple' object does not support item assignment
print(dimensions)
# 元组中的变量不能改变  但是元组本身可以重新赋值
dimensions = (1, 3, 11)
print(dimensions)