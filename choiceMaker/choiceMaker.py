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
        #通过flag和time参数，实现一小时只能抽一次签
        self.flag = 0 
        self.time = 0
        #初始化全局变量
        self.events = ["生命不息，脑洞不止", "来一发PAT吧", "忘记工作，玩会游戏", "阅读图书","现在是英语听力时间","艺群相关工作"]#事件列表
        self.numEvents = len(self.events)
        #文本路径
        self.recordPath = r"record.txt"
        
        
        #标题
        self.lb1 = Label(self.frame, text = '往期回顾', justify=CENTER)  
        self.lb1.grid(row = 1, column = 1)  
        #消息框1
        self.listbox1 = Listbox(self.frame, width = 28, height = 6)  
        self.listbox1.grid(row = 2, column = 1, sticky = N, padx=10, pady=5)#padx和pady决定文本框上下左右空出多大像素的间隔
        #消息框2
        self.listbox2 = Listbox(self.frame, width = 28, height = 1, justify=CENTER)#justify参数决定了文本显示是靠左右对齐还是居中  
        self.listbox2.grid(row = 3, column = 1, sticky = N, padx=10, pady=5)         
        #抽选按钮
        self.btnChoice = Button(self.frame, text = 'make choice', command = self.makeChoice)  
        self.btnChoice.grid(row = 4, column = 1, sticky = W+E+N, padx=5, pady=5)  
        self.loadRecord()
    
    def loadRecord(self):
        f=open(self.recordPath)
        lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '')
            self.listbox1.insert(END, line)
        self.listbox1.itemconfig
    
    def makeChoice(self):
        '''
        随机抽取时间并显示出来
        '''
        self.index = random.choice(list(range(self.numEvents)))#随机抽取
        self.list2 = self.events[self.index]
        if self.flag == 0:
            self.time = time.time()
            self.flag = 1
            self.listbox2.insert(END, self.list2)
        else:
            #如果在1小时内多次抽取，则拒绝请求
            if time.time()-self.time <3600:
                self.list2 = "请不要在1小时内重复抽取"
            self.listbox2.delete(0)
            self.listbox2.insert(END, self.list2)

        self.listbox2.itemconfig


if __name__ == '__main__':  
    root = Tk()  
    tool = decisionMaker(root)  
    root.mainloop()
