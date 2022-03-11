import random  #产生随机数
serect=random.randint(1,10) #产生1到10内的随机数
i=0
team=input('请输入一个你喜欢的数字：\n')
guess=int(team)
while guess!=serect and i<2:    #&&不能用  and和&&作用一样
    team=input('猜错了，请重新猜\n')
    guess=int(team)
    if guess==serect:
        print("你竟然猜中了")
    else:
        if guess>serect:
            print("你猜的数字大了")
        else:
            print("你猜的数字小了")
    i=i+1
print("游戏结束\n")
print('这个数字为',serect)
