import math
'''
# celi() 向上取整操作
print(math.ceil(5.06))
print(math.ceil(5.9))

# f0loor()向下取整操作
print(math.floor(5.06))
print(math.floor(5.9))
'''

'''
import keyword #查看系统保留关键字
ls =keyword.kwlist
print(ls)
'''

'''
#round()四舍五入操作
print(round(5.01))
print(round(5.5))
 '''

'''
#sqrt() 开平方，返回浮点数
print(math.sqrt(4))
'''

'''
#pow() 与幂运算差不多,两个参数第一个是底数，第二个是指数
print(math.pow(3,5))#3的5次方 返回的是浮点型
'''

#随机数模块
import random
# random() 获取0-1之间的随机小数，包含0不包含1
for i in range(5):
    print(random.random())
    print(random.randint(1,9))


