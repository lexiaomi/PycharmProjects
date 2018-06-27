# 包含一个学生类，一个sayhello,一个打印语句

class Student():
    def __init__(self,name="Noname",age=18):
        self.name = name
        self.age = age

    def Sayhello(self):
        print("我说话了")

def say():
    print("欢迎来到我的modoul")
# 判断语句建议一直作为程序的入口
if __name__ == '__main__':

    print("go,go,go")
