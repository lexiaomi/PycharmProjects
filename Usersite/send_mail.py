from django.core.mail import send_mail
import os
# 通过os模块对环境变量进行设置
os.environ['DJANGO_SETTINGS_MODULE'] = 'Usersite.settings'

if __name__ == '__main__':

    send_mail(
        '来自www.lilijunblog.com的测试邮件',
        '欢迎访问www.lilijun.com，这里是刘江的博客和教程站点，本站专注于Python和Django技术的分享！',
        '18773681292@163.com',
        ['18773681292@163.com'],
    )