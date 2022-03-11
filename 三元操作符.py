x,y=4,5
if x<y:
    shall=x
else:
    shall=y
print(shall)
#可以改进为
shall=x if x<y else y
print(shall)
