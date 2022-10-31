def fun(a,b):
    
    def inFun():
        r=a+b
        return r
    
    return a,inFun

ruslt,first=fun(7,7)
print(ruslt)
ruslt,temp=fun(2,2)
print(ruslt)
ruslt,temp=fun(3,3)
print(ruslt)
ruslt,temp=fun('a','a')

print('-'*20)
print(first())
print(first)
print(temp())
print(temp)
