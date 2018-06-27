'''
掌握对url进行参数编码的方法
需要使用parse模块
'''

from urllib import request,parse

if __name__ == '__main__':
    url = "https://www.baidu.com/s?"
    wd = input("请输入你的值：")

    qs = {
        "ie":wd
    }
    qs = parse.urlencode(qs)
    print(qs)

    fulurl = url + qs
    print(fulurl)

    rsp = request.urlopen(fulurl)

    html = rsp.read()
