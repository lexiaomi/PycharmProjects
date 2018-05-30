from selenium import webdriver
import csv
#网易云音乐歌单第一页的url
url =  'http://music.163.com/#/discover/playlist/'\
        '?order=hot&cat=全部&limit=35&offset=0'
#用PhantomJS接口创建一个selenium的webdriver
driver = webdriver.PhantomJS()
#准备好存储歌单的csv文件
csv_file = open("playlist.csv","w",newline='')
writer = csv.writer(csv_file)
writer.writerow(['标题','播放数','链接'])
#解析每一页，直到‘下一页’为空
while url != 'javascript:void(0)':
    #用webdriver加载页面
    driver.get(url)
    #切换到内容
    driver.switch_to.frame("contentFrame")
    #定位歌单标签
    data = driver.find_element_by_id("m-pl-container"). find_elements_by_class_name("u-cover u-cover-1")
    for i in range(len(data)):
        #获取播放数
        nb = data[i].find_element_by_class_name("nb").text
        if '万' in nb and int(nb.split("万")[0])>500:
            #获取超过500万的
            msk = data[i].find_element_by_css_selector("a.msk")
            #标题与链接一起写入文件中
            writer.wirterow([msk.get_attribute('title'),nb,msk.get_attribute('href')])
    #定位下一页的url
    url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute('href')
csv_file.close()
