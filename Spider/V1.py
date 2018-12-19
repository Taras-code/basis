from urllib import request
if __name__ == '__main__':
    url = 'https://translate.google.cn/'
    wd = input("Input your keyword:")


    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)
    print("URL：{0}".format(rsp.geturl()))
    print("Info：{0}".format(rsp.info()))
    print("Code：{0}".format(rsp.code()))
    html = rsp.read()
    html = html.decode()
