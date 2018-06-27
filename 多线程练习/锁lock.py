import threading

sum = 0
loopSum = 1000000

lock = threading.Lock()

def myAdd():
    global sum,loopSum
    for i in range(1,loopSum):
        lock.acquire()# 上锁
        sum += 1
        lock.release()# 释放锁


def myMinu():
    global sum,loopSum
    for i in range(1,loopSum):
        lock.acquire()  # 上锁
        sum -= 1
        lock.release()  # 释放锁


if __name__ == '__main__':
    print(" Starting.....{0}".format(sum))

    t1 = threading.Thread(target=myAdd,args=())
    t2 = threading.Thread(target=myMinu,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("结束.....{0}".format(sum))
