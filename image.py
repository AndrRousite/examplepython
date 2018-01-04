# 爬取图片
import urllib.request

import re

import os

request = urllib.request.Request("http://www.douban.com/")
response = urllib.request.urlopen(request)

data = response.read()


def savefile(path):
    if not os.path.isdir("./resource/img"):
        os.mkdir("./resource/img")

    return os.path.join("./resource/img", path[path.rindex('/') + 1:])
    pass


for link, t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):
    print(link)
    try:
        urllib.request.urlretrieve(link, savefile(link))
    except Exception as e:
        print("保存失败: ", e)
