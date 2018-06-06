'''
定义一个学生类，用来形容学生
'''
#定义一个空的学生类
class Student():
    pass
# 定义一个对象
lilijun = Student()

# 再定义一个类，用来描述听python的学生
class PythonStudent():
    # None给不确定的值赋值
    name = None
    age = 22
    course = "Python"
    # 注意事项
    # 1.def homework的缩进层数
    # 2.系统默认有一个self参数
    def dohomework(self):
        print("I do zuoye")

        # 推荐在函数末尾使用return语句
        return None
# 动作实例化
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
#需要注意成员函数的调用没有传入参数
yueyue.dohomework()

class Math():
    sourcce = 33
    kechenghao = 19293

tt = Math()
print(Math.kechenghao)
print(Math.sourcce)


