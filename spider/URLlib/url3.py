# urlopen 返回对象
# geturl,info,getcode
import urllib.request
if __name__ == '__main__':
    url = "https://www.sogou.com/sogou?query=%E7%BD%91%E6%98%93%E4%BA%91%E8%AF%BE%E5%A0%82&ie=utf8&pid=sogou-site-f82a944b799eac19"

    response = urllib.request.urlopen(url)
    print(type(response))
    print(response)

    print("URL:{0}".format(response.geturl()))
    print("Info:{0}".format(response.info()))
    print("Code:{0}".format(response.getcode()))
    html = response.read()
    html  = html.decode()