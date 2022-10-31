# l1=[
#     {'name':'xiaohu','damage':2200},
#     {'name':'Tian','damage':4397},
#     {'name':'clearLove','damage':4396},
#     {'name':'kid','damage':443},
#     ]


# lam=lambda x:x['damage']

# # lMax=max(l1,key=lam)
# # lMax=max(l1,key=lam)
# for i in l1:
#     if lam(i)>2200:
#         print(i['name'])

# # print(lMax)


###############################################
# l1=[5,-62,0,55,62,1,2,-66]

# r=list(map(lambda x:x if x % 2==0 else x+2,l1))

# print(l1)
# print(r)

###############################################
# import operator

# # r=list(map(lambda x,y:x+y,range(1,6),range(1,6)))
# r=list(map(str,range(1,3)))
# print(r)
# r=list(map(lambda x,y:str(x)+str(y),range(1,7),range(1,7)))

# print(r)

# print(type(input))
# input=3
# print(type(input))
# from functools import reduce

# l1=['1','2','3','4','5','6','7','8','9','10']
# r=reduce(lambda x,y:x+y,l1)
# print(r)


##########################################################################
l1=[
    {'name':'xiaohu','damage':2200},
    {'name':'Tian','damage':4397},
    {'name':'clearLove','damage':4396},
    {'name':'kid','damage':443},
    ]
l1 = list(filter(lambda x:x['damage']>1000,l1))
print(l1)
# [{'name': 'Tian', 'damage': 4397}, {'name': 'clearLove', 'damage': 4396}]
l1=sorted(l1,key=lambda x:x['damage'])
# l1.reverse()
print(l1)
