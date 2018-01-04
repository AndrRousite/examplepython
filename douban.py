import urllib.request


def save_file(byte, name):
    path = "./resource/" + name + ".html"
    f = open(path, "wb")
    f.write(byte)
    f.close()


url = "http://www.taobao.com/"

request = urllib.request.Request(url)

response = urllib.request.urlopen(request)

data = response.read()

save_file(data, "taobao")

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())
