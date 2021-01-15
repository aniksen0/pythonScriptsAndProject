# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 03:31:34 2021

@author: Anik
"""

from tkinter import *
from tkinter.ttk import *
from time import strftime

root =Tk()
root.title("Clock:")
root.configure(bg='black')

def time():
    string =strftime("%H:%M:%S %p")
    string2 =strftime("%m-%d-%Y")
    label.config(text=string)
    label2.config(text=string2)
    label.after(1000,time)
    

label=Label(root,font=("ds-digital",80),background="black",foreground="cyan")
label2=Label(root,font=("ds-digital",40),background="black",foreground="cyan")
label.pack(anchor='center')
label2.pack(anchor='center')
time()
mainloop()