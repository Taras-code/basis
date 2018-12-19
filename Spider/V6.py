from urllib import request, error
if __name__== '__main__':
    url = "https://www.baidu.com/"
    try:
        rep = request.Request(url)
        rsp = request.urlopen(rep)
        html = rep.read().decode()
        print(html)
    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))
    except Exception as e:
        print(e)

