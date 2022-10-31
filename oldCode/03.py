#生成十个随机数并且依次存入列表中

import random

randList=[]
for i in range(10):
    while True:
        n=random.randint(1,10)#生成随机数n

        '''方法1
        flag=True             #判断n是否符合条件
        for i in range(len(randList)):
            if n==randList[i]:
                flag=False
                break         
        
        if flag==True:        #符合条件
            randList.append(n)        
            break
        '''
        #方法2
        flag = n in randList
        if not flag:
            randList.append(n)
            break
    

print(randList)

