
class Finsh():
    def __init__(self,name):
        self.name = name
    def swim(self):
         print("I am Swimming ...")
class Bird():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print("T am flying")

class Person():
    def __init__(self,name):
        self.name=name
    def study(self):
        print("good good study,day day up!")
# 多继承
#经典问题：菱形问题
# 使用中推荐不使用多继承
class SuperMan(Person,Finsh,Bird):#括号里的父类有一定顺序
    def __init__(self,name):
        self.name = name

p = SuperMan("lili")
p.fly()
p.study()
p.swim()


# 单继承
# 可以使用父类的成员方法和私有属性
class Student(Person):
    def __init__(self,name):
        self.name = name

t = Student("JJ")
t.study()

