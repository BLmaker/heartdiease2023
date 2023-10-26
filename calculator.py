# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:49:49 2023

@author: jlee150
"""

from tkinter import *

root=Tk()
root.title("Simple Calculator")

e=Entry(root, width=50, borderwidth=35, border=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10 )



#e.pack()
#e.insert(0, "number") # 이것은 블랭크에 한거




def button_add(number):
    #e.delete(0, END) # 블랭크를 지워줌
    
    e.insert(0, number)
    return

# define buttons 




button_1=Button(root, text="1", padx=40, pady=20, command=lambda: button_add(1))
button_2=Button(root, text="2", padx=40, pady=20, command=lambda: button_add(2))
button_3=Button(root, text="3", padx=40, pady=20, command=lambda: button_add(3))
button_4=Button(root, text="4", padx=40, pady=20, command=lambda: button_add(4))
button_5=Button(root, text="5", padx=40, pady=20, command=lambda: button_add(5))
button_6=Button(root, text="6", padx=40, pady=20, command=lambda: button_add(6))
button_7=Button(root, text="7", padx=40, pady=20, command=lambda: button_add(7))
button_8=Button(root, text="8", padx=40, pady=20, command=lambda: button_add(8))
button_9=Button(root, text="9", padx=40, pady=20, command=lambda: button_add(9))
button_0=Button(root, text="0", padx=40, pady=20, command=lambda: button_add(0))

button_add=Button(root, text="+", padx=40, pady=20, command=lambda: button_add())
button_equal=Button(root, text="=", padx=80, pady=20, command=lambda: button_add())
button_clear=Button(root, text="CLS", padx=80, pady=20, command=lambda: button_add())


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

# put the bottuons on the scrren


#myButton=Button(root, text='click', command=myClick, fg='blue') #,state=DISABLED) 스테이츠를 누르면 디저블드
#myButton.pack()



root.mainloop()
