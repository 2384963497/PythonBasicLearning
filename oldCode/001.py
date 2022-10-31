n=input("请输入数据：")

if n.isdigit():                                                  #数字情况
    sum=0
    for i in range(int(n)+1):
        sum+=i
    print("累加和为：{}".format(sum))
elif (n[0]==n[-1] and n[0]=='"') or (n[0]==n[-1] and n[0]=="'"): #字符情况
    for i in n:
        print(i)
else:                                                            #其他情况
    print("不予处理！")
