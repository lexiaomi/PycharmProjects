from multiprocessing import  Process
import  time

def run(num):
    while True:
        print("进程开始时间{0}".format(time.ctime()))
        time.sleep(num)


if __name__ == '__main__':
    p = Process(target=run,args=(3,))
    p.start()

    while True:
        print("休息。。。。")
        time.sleep(2)
