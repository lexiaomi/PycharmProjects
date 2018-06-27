import threading
import time

semaphore = threading.Semaphore(3)


def fun_c():
    if semaphore.acquire():
        for i in range(3):
            print(threading.currentThread().getName()+' get semaphore')
        time.sleep(10)
        semaphore.release()
        print(threading.currentThread().getName() + ' release semaphore')


for i in range(10):
    t1 = threading.Thread(target=fun_c)
    t1.start()