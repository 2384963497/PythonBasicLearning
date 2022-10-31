#随机生成两个长度为10的元素范围为[1,30]的集合；并且将两个集合中不同的元素存放在set3中
import random
set1=set()
set2=set()

while len(set1)<10:
    n=random.randint(1,30)
    set1.add(n)

while len(set2)<10:
    n=random.randint(1,15)
    set2.add(n)
#############################################

set3=set1.union(set2)
set3=set3-(set3&set1)

print(set1,set2,set3,sep='\n')
