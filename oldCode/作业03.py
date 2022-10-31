n = int(input("请输入需要输出的行数:"))

i=n
while i>=-n:
    for j in range(abs(i)):
        print(' ',end='')
    for j in range(2*(n-abs(i))-1):
        print('*',end='')
    i-=1
    print('')
