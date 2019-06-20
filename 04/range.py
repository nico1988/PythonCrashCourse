for value in range(1,22):
    print(value)

# 指定步长
print("指定步长方式")
for value in range(1,33,9):
    print(value)

# 生成1-10的平方数
squares=[]
for value in range(1,11):
    squares.append(value**value)
print(squares)

# 数学计算

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 一行代码生成1-10的平方数组
s=[v**2 for v in range(1,11)]
print(s)

print([range(1,21)])

# 输出100 0000
million=[v for v in range(1,1000001)]
# 打印基数
ee= range(1,21,2)
for e in ee:
    print(e)

aa=range(3,31,3)
for a in aa:
    print(a)
bb=[v**3 for v in range(1,11)]
print(bb)
