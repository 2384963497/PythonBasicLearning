#找出列表的最大值

def list_max(inlist):
    max=inlist[0]
    for i in inlist:
        if max<i:
            max=i
    return max
l=list()

n=eval(input("请输入列表的值(以任意非数字字符结束):"))
while isinstance(n,int):
    l.append(n)
    n=eval(input("请输入列表的值(以任意非数字字符结束):"))

print(l)
maxNum=list_max(l)
print(maxNum)