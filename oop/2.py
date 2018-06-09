# user/bin/lilijun
#2018-5-30
# oop2
# class A():
#     name = "kkk"
#     age = 18
# print(A.age)
# print(A.name)
# print("--"*20)
# a = A()
# print(A.__dict__)
# print(a.__dict__)
# a.name = "zhouzhou"
# a.age = 20
# print(a.__dict__)
# print(a.age)
# print(a.name)

# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
# t = Test()
# t.prt()

'''class Emp loyee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print( "Total Employee {0}".format(Employee.empCount))


    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)



"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee{0}".format(Employee.empCount) )'''

'''class Student:
    name = "yueyue"
    age = 18
    def say(self):
        self.name = "yueyue"
        self.age = 18
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))
llj = Student()# 类实例化
llj.say() #调用方法'''

# class Teacher:
#     name = "LL"
#     age = 22
#     def say(self):
#         self.name = "LLJ"
#         self.age = 19
#         print("my name is {0}".format(self.name))
#         print("my age is {0}".format(self.age))
#     def sayAgain(s):
#         print("hello , is me")
# t = Teacher()
# t.say()
# t.sayAgain()

class T:
    add = "wuhan"
    num = 12
    def green(self):
        print(self.num)
        print(self.add)
    def __red(self):#私有对象定义
       print(self.num)
       print(self.add)

r = T()
r.green()
r._T__red()#对私有对象的访问
