a=input('请输入数据：')
if a[0]>='0' and a[0]<='9':
    s=0
    a=int(a)
    for i in range(a+1):
        s+=i
    print("累加为:{}".format(s))
elif a[0]==a[-1] and a[0]=='"' or a[0]==a[-1] and a[0]=="'":
    for i in a:
        print(i)
else:
    print("不予处理！")