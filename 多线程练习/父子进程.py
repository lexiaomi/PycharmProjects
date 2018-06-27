from multiprocessing import Process
import os


def info(title):
    print(title)
    print("moudlename:",__name__)
    print("父进程ID：",os.getppid())
    print("子进程ID：",os.getpid())


def f(name):
    info("函数f")
    print('hai',name)


if __name__ == '__main__':
    info("主进程")
    p = Process(target=f,args=("lili",))
    p.start()
    p.join()