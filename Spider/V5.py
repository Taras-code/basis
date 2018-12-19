from urllib import request, parse

import json
baseurl = 'https://fanyi.baidu.com/sug'
data = {
        'kw': 'girl'
    }
data = parse.urlencode(data).encode("utf-8")
print(data)
headers = {
    'Content-Length': len(data)
}
# rsp = request.urlopen(baseurl, data=data)
req = request.Request(baseurl, data=data, headers=headers)
rsp = request.urlopen(req)
json_data = json.loads(rsp.read().decode())
for i in json_data['data']:
    print(i['k'], "--", i['v'])
