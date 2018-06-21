'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间

'''
import time


def loop1():
    print("loop1开始运行时间",time.ctime())
    time.sleep(3)
    print("loop1结束运行时间",time.ctime())


def loop2():
    print("loop2开始运行时间",time.ctime())
    time.sleep(5)
    print("loop2结束运行时间",time.ctime())


def main():
    print("main开始运行时间",time.ctime())
    loop1()
    loop2()
    print("main结束运行时间",time.ctime())


if __name__ == '__main__':
    main()

