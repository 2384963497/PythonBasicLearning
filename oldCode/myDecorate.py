import time
import os

#登录检测 装饰器
def loginRequired(func):
    def check(*args,**kwargs):
        if loginFlag==True:
            func(*args,**kwargs)
        else:
            print("用户未登录请登录后再试")
            print("选择完成(2s后返回)")
            time.sleep(2)
    return check
                

#加入购物车
@loginRequired
def IntoCar(*args,**kwargs):
    global carGoods
    print("{}，成功加入购物车！".format(kwargs))
    carGoods.update(kwargs)
#支付
@loginRequired
def payGoods(*args,**kwargs):
    print("-"*8+'请支付{}元'.format(args)+'-'*8)
    payFlag=input("是否确定支付:(Y/N)")
    
    if payFlag in 'Yy':
        print("正在支付......")
        time.sleep(2)
        print("支付成功")
    else:
        print("支付已取消")
#1.登录账号
def loginFunc():
    global loginFlag
    while True:
        os.system("cls")
        print('-'*30)
        userName=input("请输入用户名:")
        passWord=input("请输入密码:")

        if userName=='xiaohu' and passWord=='2200':
            loginFlag=True
            print("登录成功！(2s后返回)")
            time.sleep(2)
            return
        else:
            userInput=input("用户名或密码输入有误！是否重试(Y/N):")
            if userInput in 'Yy':
                continue
            else:
                return

#2.选择商品
@loginRequired
def selectFunc():
    global selectedGoods
    selectedGoods={}
    os.system("cls")
    #打印商品
    Goods={'1':('不朽盾弓',3400),'2':("海妖杀手",3400),'3':("渴血战斧",3300),'4':('兰顿之兆',2700)}
    for i in Goods:
        print("{}:{}售价{}\n".format(i,Goods[i][0],Goods[i][1]))
    print("-"*30)
    #选择商品
    
    temp=input("请输入需要选择的装备序号(之间用一个空格隔开)")
    temp=temp.split(' ')
    # print(temp)
    #将选择商品添加到元组
    for i in temp:
        selectedGoods[Goods[i][0]]=Goods[i][1]
    print("选择完成(2s后返回)")
    time.sleep(2)



#3.添加商品到购物车
#4.删除购物车商品
@loginRequired
def delGoods():
    pass
#5.购买购物车所有商品

###############################################################################
selectedGoods={}
carGoods={}
loginFlag=False
while True:
    os.system("cls")
    print('-'*30)
    print('''
    1.登录账号
    2.选择商品
    3.添加商品到购物车
    4.删除购物车商品
    5.购买购物车所有商品
    6.退出程序
    ''')

    userInput=int(input("请选择操作序号:"))
    if userInput==1:
        loginFunc()
    elif userInput==2:
        selectFunc()
        print(selectedGoods)
        input()
    elif userInput==3:
        IntoCar(**selectedGoods)
        print(carGoods)
        input()
    elif userInput==4:
        delGoods()
    elif userInput==5:
        if not carGoods:
            print("购物车里还没有商品！请选择后再试")
            print("2s后返回")
            time.sleep(2)
        else:
            sum=0
            print(carGoods)
            for i in carGoods:
                sum+=carGoods[i]
            payGoods(sum)
    elif userInput==6:
        break
    else:
        userInput=input("输入有误！是否重新输入(Y/N):")
        if userInput in "Yy":
            continue
        else:
            break

os.system("cls")
print("程序运行结束!")