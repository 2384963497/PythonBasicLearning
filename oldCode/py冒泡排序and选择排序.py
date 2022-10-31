#随机生成n个 0-100的无重复随机数  冒泡排序(降序)后输出  n输入获得
import random
randList=[]
n = eval(input("请输出需要输出的列表长度:"))
i=0
while i<n:
    e=random.randint(0,100)
    if e not in randList:
        randList.append(e)
        i+=1
print("生成后原列表：\n{}".format(randList))

# for i in range(n):        #冒泡排序
#     for j in range(i+1,n):
#         if randList[i]<randList[j]:
#             randList[j],randList[i]=randList[i],randList[j]

#选择排序
for i in range(n-1):
    pos=i
    for j in range(i+1,n):
        if randList[pos]<randList[j]:
            pos=j
    if pos!=i:
        randList[pos],randList[i]=randList[i],randList[pos]

print("排序后为：\n{}".format(randList))
