n=input("请输入数据：")

if n.isdigit():
    sum=0
    for i in range(int(n)+1):
        sum+=i
    print("累加和为：%d"%(sum))
elif n.isalpha():
    for i in n:
        print(i)
else:
    print("不予处理！")
