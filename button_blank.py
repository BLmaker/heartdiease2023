# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:49:49 2023

@author: jlee150
"""

from tkinter import *

root=Tk()


e=Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter your name") # 이것은 블랭크에 한거

def myClick():
    hello="hello "+e.get()
    myLabel=Label(root, text=hello)
    myLabel.pack()


myButton=Button(root, text='click', command=myClick, fg='blue') #,state=DISABLED) 스테이츠를 누르면 디저블드
myButton.pack()



root.mainloop()
