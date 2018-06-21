import time, threading

size = 0
count = 10

#锁对象
lock = threading.Lock()

def set_size():
    global size
    #加锁
    #lock.acquire()
    try:
        for x in range(0,1000):
            size += 1
            size -= 1
    finally:
        #释放锁
        #lock.release()
        pass

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    set_size()
    print('thread %s is '% threading.current_thread().name, size)

def runr():
    global count
    print('thread %s is running...' % threading.current_thread().name)
    for x in range(0,count):
        t = threading.Thread(target=loop, name=('LoopThread ' + str(x)))
        t.start()
        t.join()

    print('thread %s ended.' % threading.current_thread().name)
    print(size)


runr()


