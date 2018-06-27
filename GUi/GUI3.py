#菜单
# 1.普通菜单
# 第一个Menu类的定义是parent
#add_command 添加菜单项，如果菜单是顶层菜单，则从左向右添加，否则就是下拉菜单
#   label：指定菜单单项名称
#   command：点击后调用相应的函数
#   acceletor：快捷键
#   underline：指定是否菜单信息下有横线
#   menu：属性指定使用哪一个作为顶级菜单

import tkinter

baseFrame = tkinter.Tk()

menubar = tkinter.Menu(baseFrame)

for item in ['首选项','编辑','查找','关于']:
    menubar.add_command(label=item)


baseFrame['menu'] = menubar


baseFrame.mainloop()