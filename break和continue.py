#break 和 continue 作用和C语言一样
print(list(range(10)))
for i in range(10):
    if i%2!=0:
        print(i)
        continue
    i+=2
    print(i)
