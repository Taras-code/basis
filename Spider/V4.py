from urllib import request
if _name_ == '_main_':
    url ='https://translate.google.cn/s?'
    wd = input("Input your keyword:")
    qs = {
        "wd": wd
    }
    qs = parse.urlencode(qs)
    fullurl = url + qs

    rsp = urllib.request.urlopen(fullurl)

    print(type(rsp))
    print(rsp)
    print("URL：{0}".format(rsp.geturl()))
    print("Info：{0}".format(rsp.info()))
    print("Code：{0}".format(rsp.code()))
    html = rsp.read()
    html = html.decode()
