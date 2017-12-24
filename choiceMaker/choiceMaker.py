import os
import random
import time
from tkinter import *

class decisionMaker():
    def __init__(self, master):
        #创建主要框架
        self.parent = master
        self.parent.title("decisionMaker")
        self.frame = Frame(self.parent)  
        self.frame.pack(fill=BOTH, expand=1)  
        self.parent.resizable(width = False, height = False)
        
        #初始化全局变量
        self.events = ["生命不息，脑洞不止", "来一发PAT吧", "忘记工作，玩会游戏", "阅读图书","现在是英语听力时间","艺群相关工作"]#事件列表
        self.numEvents = len(self.events)
        
        #标题
        self.lb1 = Label(self.frame, text = '往期回顾')  
        self.lb1.grid(row = 1, column = 1,  sticky = W+N)  
        #消息框1
        self.listbox1 = Listbox(self.frame, width = 28, height = 12)  
        self.listbox1.grid(row = 2, column = 1, sticky = N)
        #消息框2
        self.listbox2 = Listbox(self.frame, font = ('Arial,12'), width = 28, height = 1)  
        self.listbox2.grid(row = 3, column = 1, sticky = N)         
        #抽选按钮
        self.btnChoice = Button(self.frame, text = 'make choice', command = self.makeChoice)  
        self.btnChoice.grid(row = 4, column = 1, sticky = W+E+N)  
        
    def makeChoice(self):
        self.index = random.choice(list(range(self.numEvents)))#随机抽取
        self.FLAGS = self.events[self.index]
        self.listbox2.insert(END, self.FLAGS)
        self.listbox2.itemconfig

if __name__ == '__main__':  
    root = Tk()  
    tool = decisionMaker(root)  
    root.mainloop()
