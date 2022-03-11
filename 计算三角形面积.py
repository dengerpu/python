a=input('请输入a的值:')
b=input('请输入b的值:')
c=input('请输入c的值:')
a=int(a)
b=int(b)
c=int(c)
p=int(a+b+c)/2
import math
s=math.sqrt (p*(p-a)*(p-b)*(p-c))
print(s)
