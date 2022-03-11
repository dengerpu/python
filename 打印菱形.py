n=input('请输入n的值')
n=int(n)
for i in range(1,n+1):   #第1到n行
    for j in range(n-i):  #打印n-i个空格
        print(end=' ')
    for k in range(2*i-1):  #打印2*i-1个*
        print(end='*')
    print('\n')
m=n-1;
"""for i in range(1,n):   #只需要再打印n-1行
    for j in range(i):
        print(end=' ')
    for k in range(2*m-1):
        print(end='*')
    m=m-1;
    print('\n')"""
