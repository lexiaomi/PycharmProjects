'''
练习：输入一个三位数与随机数比较大小
1.如果大于程序随机数，则分别打印出这个三位数的个十百位
2，如果相等，则提示中奖
3，如果小于，则将120个字符输入到文本文件中
（规则是每一条字符串长度为12，单独占一行，且前面是字母，后面是数字

'''

import random
import math
#定义一个变量用于存取初始分数
source = 0
# 定义一个变量用于累计输入次数
total = 0


def num_game(total,source):
    while 1:
        num = input("请输入一个三位数：")
        if num == '-1':
            break
        random_num = random.randrange(100,1000)

        def line():
            #定义一个空字符串，用于拼接
            str_num = " "
            # 循环四个随机字母（用ASCII码值来转换）
            for i in range(4):
                num = random.randrange(97,123)
                str_zm = chr(num)
                str_num = str_num + str_zm
            #print(str_num)

        # 循环后面8位数字
            for i in range(8):
                num = random.randrange(0,10)
                str_num = str_num + str(num)
                # print(str_num)
            return str_num

        if num.isdigit() and 100<=int(num) <=999:
            total += 1
            print("有效输入次数%d"%total)
            num = int(num)
            random_num = int(random_num)
            if num > random_num:
                ge = num%10
                shi = num%100//10
                bai = num//100
                print("你输入的数比程序随机数大，程序随机数是",random_num)
                print("个位是{0}，十位是{1}，百位是{2}".format(ge,shi,bai))

            if num == random_num:
                source = source+100
                print("您中奖了,你的目前分数为",source)
                print("你中奖的概率是",source/total)

            if num < random_num:
                for i in range(10):
                    str_line = line()
                    #print(str_line)
                    with open('str_num.txt','a') as f:
                        f.write(str_line+'\n')
                        f.close()
                print("你输入的数比程序随机数小，程序随机数是", random_num)
        else:
            print("请输入正确的值!!!!!")


#程序入口
if __name__ == '__main__':
    num_game(total,source)
