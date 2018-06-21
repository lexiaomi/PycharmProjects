
# _thread的使用
# 传入参数的使用
import _thread as thread
import time


def loop1(in1):
    print("loop1 开始运行时间：",time.ctime())
    print("参数1",in1)
    time.sleep(3)
    print("loop1结束运行时间：",time.ctime())


def loop2(in1,in2):
    print("loop2 开始运行时间：",time.ctime())
    print("参数1",in1,"和参数2",in2)
    time.sleep(4)
    print("loop2结束运行时间：",time.ctime())


def main():
    print("main 开始运行时间：",time.ctime())
    thread.start_new_thread(loop1 , ("liliun",))
    thread.start_new_thread(loop2 , ("lilijun","容建波love？？？",))
    print("全部结束运行的时间：",time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)