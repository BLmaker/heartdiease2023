# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:36:28 2023

@author: jlee150
"""

from tkinter import *
root=Tk()

myLabel1=Label(root, text="babo").grid(row=0, column=0)
myLabel2=Label(root, text="babo2").grid(row=0, column=1)

#myLabel.pack()

#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=0) # 팩은 하나 그리드는 하나. 
root.mainloop()