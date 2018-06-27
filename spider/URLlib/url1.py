import urllib.request
if __name__ == '__main__':
    url = "http://study.163.com/my"
    response = urllib.request.urlopen(url)
    html = response.read()
    print(html)

