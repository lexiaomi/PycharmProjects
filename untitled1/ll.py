import requests
response = requests.get('https://www.bilibili.com/video/av22028273?p=4')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(type(response.cookies))

