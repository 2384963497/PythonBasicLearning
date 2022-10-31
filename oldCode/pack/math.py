print("math模块被读入啦!!!")

def adds(a,b):
    return a+b

def minus(a,b):
    return a-b

def times(a,b):
    return a*b

def divide(a,b):
    try:
        return a/b
    except Exception:
        print("数据错误！！不符合要去 ")
        return None

def display():
    print(__name__)

display()



