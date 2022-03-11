#range()    range([strat,]stop[,step=1])
#有三个参数 中括号括起来的两个参数是可选的
#seep=1表示第三个参数的值默认值是1
#range这个bif的作用是生成一个从start参数的值开始到stop参数的值结束的数字序列
range(5)
print('range 有一个参数\n')
print(list(range(5)))
print('range 有两个参数\n')
print(list(range(2,9)))
for i in range(2,9):
    print(i)
print('range 有三个参数\n')
print(list(range(1,10,2)))
for i in range(1,10,2):
    print(i)

