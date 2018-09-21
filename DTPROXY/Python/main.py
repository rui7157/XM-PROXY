# 新用户只需要替换14行和15行的orderno和secret即可运行

import sys
import time
import hashlib
import requests
from lxml import etree

_version = sys.version_info

is_python3 = (_version[0] == 3)

# 个人中心获取orderno与secret
orderno = "DT20179xxxxxxxxx"    
secret = "3f9c2ecac7xxxxxxxxxxxxxxxx"

ip = "dynamic.xiongmaodaili.com"
port = "8089"

ip_port = ip + ":" + port

timestamp = str(int(time.time()))                # 计算时间戳
txt = ""
txt = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp

if is_python3:
    txt = txt.encode()

md5_string = hashlib.md5(txt).hexdigest()                 # 计算sign
sign = md5_string.upper()                              # 转换成大写
print(sign)
auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp

print(auth)
proxy = {"http": "http://" + ip_port}
headers = {"Proxy-Authorization": auth}
r = requests.get("https://www.baidu.com", headers=headers, proxies=proxy, verify=False,allow_redirects=False)
print(r.status_code)
print(r.content)
print(r.status_code)if r.status_code == 302 or r.status_code == 301 :
    loc = r.headers['Location']
    url_f = "https://www.baidu.com" + loc
    print(loc)
    r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    print(r.status_code)
    print(r.text)
