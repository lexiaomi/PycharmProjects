import time
import threading

def loop1(in1):
    print("loop1 开始运行时间：",time.ctime())
    print("参数1",in1)
    time.sleep(2)
    print("loop1结束运行时间：",time.ctime())


def loop2(in1,in2):
    print("loop2 开始运行时间：",time.ctime())
    print("参数1",in1,"和参数2",in2)
    time.sleep(2)
    print("loop2结束运行时间：",time.ctime())


def main():
    print("main 开始运行时间：",time.ctime())
    t1 = threading.Thread(target=loop1,args=("lilijun",))
    t1.start()
    t2 = threading.Thread(target=loop2,args=("lilihun1","llllll",))
    t2.start()
    t1.join()
    t2.join()
    print("全部结束运行的时间：",time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)