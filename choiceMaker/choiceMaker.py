import os
import random
import time
from tkinter import *

import os
import random
import time
from tkinter import *

class decisionMaker():
    def __init__(self, master):
        #创建主要变量和UI界面
        self.parent = master
        self.parent.title("decisionMaker")
        self.frame = Frame(self.parent)  
        self.frame.pack(fill=BOTH, expand=1)  
        self.parent.resizable(width = False, height = False)
        #通过flag和time参数，实现一小时只能抽一次签
        self.flag = 0 
        self.time = 0#记录上一次抽取的时间
        #初始化全局变量
        self.events = ["生命不息，脑洞不止", "来一发PAT吧", "忘记工作，玩会游戏", "阅读图书","现在是英语听力时间","艺群相关工作"]#事件列表
        self.numEvents = len(self.events)
        #文本路径
        self.recordPath = 'record.txt'
        
        
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
        #若记录文本不存在，则创立
        if not os.path.exists(self.recordPath):
            f = open(self.recordPath, 'w')
            f.close()

        self.loadRecord()
    
    def loadRecord(self):
        '''
            读取与py文件在同一目录下的record文本
        '''
        f=open(self.recordPath)
        lines = f.readlines()
        f.close()
        #若为空文本，则将上一次抽选时间设为0，并退出函数
        if lines == []:
            self.time = 0
            return
        
        #否则从第一行获取上次抽取的时间
        self.time = int(lines[-1].replace('\n', '').split(' ')[-1])#从第一行获取上一次抽取的时间
        #讲record中的记录显示在listbox1中
        for line in lines:
            #时间格式转换
            line = line.replace('\n', '').split(' ')
            t = list(time.localtime(int(line[1])))[0:6]
            a=('{}-{}-{}-{}-{}-{}'.format(t[0], t[1], t[2], t[3], t[4], t[5]))
            #先显示时间，再显示内容
            self.listbox1.insert(END, a)
            self.listbox1.insert(END, line[0])
        self.listbox1.itemconfig
        
        #在listbox2中显示欢迎语
        self.listbox2.insert(END, "welcome")
        self.listbox2.itemconfig
    
    def updateRecord(self):
        '''
        每次发生有效抽取后，讲记录写入record中，并更新listbox1的显示
        '''
        
        f=open(self.recordPath, 'a')#追加模式写文件
        intTime = str(self.time).split('.')[0]#保存time的整数部分
        f.write(self.list2 + ' ' + intTime + '\n')
        f.close()
        
        #时间格式转换
        t = list(time.localtime(int(intTime)))[0:6]
        a =('{}-{}-{}-{}-{}-{}'.format(t[0], t[1], t[2], t[3], t[4], t[5]))
        
        self.listbox1.insert(END, a)
        self.listbox1.insert(END, self.list2) #然后显示内容
        self.listbox1.itemconfig
        
    def makeChoice(self):
        '''
        随机抽取时间并显示出来
        '''
        self.index = random.choice(list(range(self.numEvents)))#随机抽取
        self.list2 = self.events[self.index]
        if time.time()-self.time <3600:
            #如果在1小时内多次抽取，则拒绝请求
            self.list2 = "请不要在1小时内重复抽取"
        else:
            #抽取间隔大于1小时，则更新时间并保存记录
            self.time = time.time()
            self.updateRecord()
            
        self.listbox2.delete(0)#清除上一次显示
        self.listbox2.insert(END, self.list2)    

        self.listbox2.itemconfig


if __name__ == '__main__':  
    root = Tk()  
    tool = decisionMaker(root)  
    root.mainloop()
