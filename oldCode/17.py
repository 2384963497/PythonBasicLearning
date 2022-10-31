
def account(func):
    print("嗨害嗨")
    def funcWarpper():
        posit={'pos':'mid'}
        print("正在校验:")
        func(**posit)
        print("交验完毕")
    return funcWarpper


@account
def fun1(**pos):
    print('='*30)
    user='xiaohu'
    passward='2200'
    print(user)
    print(passward)
    print(pos['pos'])
    print('='*30)

@account
def fun2(**bos):
    print('='*30)
    user='clearlove'
    passward='4396'
    print(user)
    print(passward)
    print(bos['pos'])
    print('='*30)


fun1()
fun2()

