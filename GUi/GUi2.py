# 消息机制
import tkinter
def baseLabel(event):
    global baseFrame
    lb = tkinter.Label(baseFrame,text="你点击了喔")
    lb.pack()


baseFrame = tkinter.Tk()
lb = tkinter.Label(baseFrame,text="模拟按钮")
lb.bind("<Button-1>",baseLabel)
lb.pack()

baseFrame.mainloop()