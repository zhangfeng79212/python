from tkinter import *  # 导入 Tkinter 库
#import tkMessageBox
import tkinter.messagebox
root = Tk()  # 创建窗口对象的背景色
root.title("日志分析")
# 创建两个列表
label1=Label(root,text="这个小程序的功能是可以分析导航菜单日志，点击分析即可在下面的text框得出分析结果")
text1=Text(root)
text2=Text(root)
def helloCallBack():
    tkinter.messagebox.showinfo('提示', '人生苦短')
button1=Button(root,text ="分析日志", command = helloCallBack)
label1.pack()
text1.pack()
button1.pack()
text2.pack()
root.mainloop()