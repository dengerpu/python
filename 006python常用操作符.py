print('+= -= *= /= 在python中也可以用')
print('在python中可以连续赋值')
a=b=c=d=10
print(a)
print(b)
print(c)
print(d)
d=d/8
print('/计算出来的结果是浮点数')
print('d/8=',d)  #整数/整数计算结果可以出现浮点数
print('//求出来是整数')
d=10
d//=8
print('d=d//8=',d)
#**代表幂
a=-3*2+5/-2-4
print('相当于((-3)*2)+(5/(-2))-4')
print(a)
print('**幂的优先级大于-负号')
print('-3**2=',-3**2)
print('(-3)**2=',(-3)**2)
print('3**-2=',3**-2)
#逻辑操作符
print('and相当于&&,or相当于||  not相当于取反')
print('3<4<5相当于3<4 and 4<5')
print(3<4 and 4<5)
print(3<4 or 5>4)
print(not 3)
#运算符优先级问题
#1. 幂运算  **
#2. 正负号 +x -x
#3. 算数运算符 * / // + -
#4. 比较运算符 < <= > >= == !=
#5. 逻辑运算符 not and or
