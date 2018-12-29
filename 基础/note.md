协程
    - 可迭代
    - 迭代器
    - 生成器
    - 协程（a = yield ，sc.send（3），so a =3）
        - inspect.getgeneratorstate(..)函数确定
        - GEN_CREATED: 等待开始执行
        - GEN_RUNNING: 解释器正在执行
        - GEN_SUSPENED: 在yield表达式处暂停
        - GEN_CLOSED: 执行结束
        - next预激（prime）
        - 哨符值（None和Ellipsis等常量）
        - yield from（委派生成器：）
re(正则表达式):
re.match() 
Xpath
-
FTP:
f.retrbinary(ftp命令，open(FILE，’wb‘).write)