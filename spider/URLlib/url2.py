import urllib.request
import chardet#自动检测编码

if __name__ == '__main__':
    url = "http://study.163.com/my"
    response = urllib.request.urlopen(url)
    html = response.read()
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    #使用get保证取值不会出错
    html = html.decode(cs.get("encoding","utf-8"))
    print(html)