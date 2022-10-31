# from ast import pattern
import re

# s="1d2d5eE3bgf51b21w2s1e21g153fgb5T6sw"

# p='[0-9][a-zA-z][0-9]'

# r = re.search(p,s)
# print(type(r))
# print(r.group())
# print(r.span())

# <class 're.Match'>
# <re.Match object; span=(0, 3), match='1d2'>



# r=re.findall(p,s)
# print(type(r))
# print(r)

# <class 'list'>
# ['1d2', '5T6']

# patt='[1]\d{10}'
# s='19132020555w'
# print(re.match(patt,s))
# patt='[1]\d{10}$'
# s='19132020555w'
# print(re.match(patt,s))

# s='apple sunny\ns12block525、？I8am chinese!'
# patt='\\b\w+\\b'
# r=re.findall(patt,s)
# print(r)

# s='19132020488'
# # patt=r'\w{5,15}@(qq|163|126)\.com$'
# patt=r'1\d{9}[^4,7]$'
# r=re.match(patt,s)
# print(r.g)

# s='023-15246215'
# patt=r'(\d{3}|\d{4})-(\d{8})$'
# r=re.match(patt,s)
# print(r.group())
# print(r.group(1))
# print(r.group(2))




# s='238496@qq.com'
# patt=r'\w{5,15}@(qq|163|126)\.com$'
# r=re.match(patt,s)
# print(r.group())
# print(r.group(1))

# msg='<html><h1>content is here</h1></html>'
# patt=r'<(?P<tag1>[A-Z0-9a-z]+)><(?P<tag2>[A-Z0-9a-z]+)>(.+)</(?P=tag2)></(?P=tag1)>$'
# # r=re.match(patt,msg)
# r=re.sub(patt,'Now，it is the new text here！',msg)
# print(msg)
# print(r)
# def func(temp):
# 	return str(int(temp.group())+1)

# score='Chinese:80 Python:79 C:52'
# # patt=r'\d+'
# patt=r'[: ]'
# r=re.split(patt,score)
# print(score)
# print(r)

# s='023-777751'
# pt='^(\d{3})-(\d{5,8})$'
# phonePt=re.compile(pt)
# print(phonePt.match(s).span())
s='"src:"www.bilibili.com";'
pt=r'src:(.+?)"'
r=re.search(pt,s)
print(r)
























