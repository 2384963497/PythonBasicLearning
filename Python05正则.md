# Python05正则表达式

[toc]



---

## 正则表达介绍

*   Regular Expression简写为re

*   作用
    *   给定字符串，判定它是否符合正则表达式的过滤逻辑
    *   可以通过正则表达式，从字符串中获取某个特定的部分


*   Python的正则通过re模块实现

---

## 匹配方法

*   `re.match(pattern,str)`

    *   从str的开头开始匹配符合正则的字符串
    *   返回一个match对象

*   `re.search(pattern,str)`

    *   在str中查询符合正则的字符串;找到第一个停止
    *   返回一个match对象

*   match对象

    *   `matchname.group()`

        *   返回匹配的对象

    *   `matchname.span()`

        *   返回匹配对象的下标范围

    *   ```python
        r = re.search(p,s)
        print(type(r))
        print(r.group())
        print(r.span())
        #<class 're.Match'>
        #1d2
        #(0, 3)
        ```

*   `re.finall(pattern,str)`

    *   在str中查询所以符合正则的字符串
    *   返回一个列表对象

*   ```python
    import re
    s="1d2d5eE3bgf51bg153fgb5T6sw"
    
    p='[0-9][a-zA-z][0-9]'
    
    r = re.search(p,s)
    print(type(r))
    print(r)
    #<class 're.Match'>
    #<re.Match object; span=(0, 3), match='1d2'>
    
    r=re.findall(p,s)
    print(type(r))
    print(r)
    #<class 'list'>
    #['1d2', '5T6']
    ```

*   `sub(pattern,repl,str)`

    *   将符合正则的字符串替换为repl；并将处理后的字符串返还；不会改变原数据的值

    *   ```python
        score='Chinese:80 Python:79 C:52'
        patt=r'\d+'
        r=re.sub(patt,'100',score)
        print(score)#Chinese:80 Python:79 C:52
        print(r)#Chinese:100 Python:100 C:100
        ```

    *   repl也可以是一个函数名

        *   ```python
            ...
            def func(temp):
            	return str(int(temp.group())+1)
            ...
            r=re.sub(patt,func,score)
            ```

*   `split(pattern,str)`

    *   在str中符合正则出进行切割；并返回切割后的列表

    *   ```python
        score='Chinese:80 Python:79 C:52'
        patt=r'[: ]'
        r=re.split(patt,score)
        print(score)#Chinese:80 Python:79 C:52
        print(r)#['Chinese', '80', 'Python', '79', 'C', '52']
        ```

*   `.compile(pattern)`

    *   可以将一个正则表达式编译为一个对象

    *   ```python
        s='023-777751'
        pt='^(\d{3})-(\d{5,8})$'
        phonePt=re.compile(pt)
        print(phonePt.match(s).span())
        ```


---

##正则通配:car:

*    `[Pya]thon`
    *   匹配Python、python或者athon
    *   []表示方括号中的任意一个元素
*    `[a-z]`
    *   [n-m]表示匹配[n,m]范围中的任意一个元素
*    `[A-Za-z0-9]`
    *   表示匹配所以字母和数字
*    [^]

    *   表示取反；即匹配不是指定的内容
    *   [^Pp]thon:匹配除了Python和python以为的其他以thon结尾的字符串
    *   [^0-8]匹配不在[0,8]以内的字符

*    `.`任意除`\n`的字符

    *    ```python
        patt='\\b\w+.'
        s='bt84lor\n74 fe\nvf'
        print(re.findall(patt,s))
        #['bt84lor', '74 ', 'fe', 'vf']
        ```

    *    `\.`匹配普通字符的 .

    *    `^`表示需要从头开始匹配


*    `$`表示需要匹配到结束

    *    ```python
        patt='[1]\d{10}'
        s='19132020555w'
        print(re.match(patt,s))#<re.Match object; span=(0, 11), match='19132020555'>
        patt='[1]\d{10}$'
        s='19132020555w'
        print(re.match(patt,s))#None
        ```


*    `\s \S`
    *    等价与`[\r\t\v\n\f]`

*    `\d \D`
    *    等价于`[0-9]`


*   `\b`

    *   匹配单词边界

    *   ```python
        s='apple sunny\n12block525、？I8am chinese!'
        patt='\\b[A-Za-z]+\\b'
        r=re.findall(patt,s)
        print(r)
        ```

    *   

*   `\w \W`
    *   等价于[0-9A-Za-z_]

*   `* + ?`

    *   `*`>=0次
    *   `+`>=1次
    *   `?`0或者1次

*   `{n} {n,m} {m,}`

    *   前面内容出现的次数

*   `|  ()`

    *   `|`分组；用法类似逻辑或

    *   `()`里面的内容分组表示

    *   ```python
        s='238496@qq.com'
        patt=r'\w{5,15}@(qq|163|126)\.com$'
        r=re.match(patt,s)
        print(r)#<re.Match object; span=(0, 13), match='238496@qq.com'>
        print(r.group())#238496@qq.com
        print(r.group(1))#qq
        ```

    *   且如果用`()`分过组；那么就可以使用match对象的.group()方法进行查看

        *   ```python
            s='023-15246215'
            patt=r'(\d{3}|\d{4})-(\d{8})$'
            r=re.match(patt,s)
            print(r.group())#023-15246215
            print(r.group(1))#023
            print(r.group(2))#15246215
            ```

    *   `()   \num  `  

        *   ```python
            msg='<html><h1>content is here</h1></html>'
            patt=r'<([A-Z0-9a-z]+)><([A-Z0-9a-z]+)>(.+)</\2></\1>$'
            r=re.match(patt,msg)
            print(r)
            print(r.group())#<html><h1>content is here</h1></html>
            print(r.group(1))#html
            print(r.group(2))#h1
            print(r.group(3))#content is here
            ```

    *   ` (?P<name>) (?P=name)`

        *   ```python
            patt=r'<([A-Z0-9a-z]+)><([A-Z0-9a-z]+)>(.+)</\2></\1>$'
            #改为：
            patt=r'<(?P<tag1>[A-Z0-9a-z]+)><(?P<tag2>[A-Z0-9a-z]+)>(.+)</(?P=tag2)></(?P=tag1)>$'
            ```




---

## 贪婪模式和非贪婪模式

*   贪婪

    *   总是尝试获得较多的字符

*   非贪婪

    *   反之
    *   加上？转为非贪婪

*   ```python
    s='"src:"www.bilibili.com";'
    pt=r'src:(.+?)"'
    r=re.search(pt,s)
    print(r)
    ```







---

##单词

*   compile  编译
*   regular expression  正则表达式