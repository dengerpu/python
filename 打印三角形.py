for i in range(5):
    for j in range(5-i+1):
        print(end=' ')    #end可以使输出不换行
    for k in range(2*i-1):
        print(end='*')
    print('\n')
    
