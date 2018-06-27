# label
import tkinter

base = tkinter.Tk()
def Hello():
    print("hello")

base.wm_title("Label Test")
lb = tkinter.Label(base,text="Python Label")
lb.pack()

lb1 = tkinter.Label(base,text="蓝色背景",background="blue")
lb1.pack()

lb2 = tkinter.Label(base,text="红色背景",background="red")
lb2.pack()
lb3 = tkinter.Button(base,text="提交",background="yellow",command=Hello)
lb3.pack()
base.mainloop()