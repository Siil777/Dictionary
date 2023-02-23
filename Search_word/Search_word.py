from tkinter import * 
import tkinter as tk 
from tkinter import ttk 


 
def add_eng():
    box2.insert(END, tk.entry.get())
    tk.entry.delete(0, END)
 
 
def del_eng():
    select = list(box2.curselection())
    select.reverse()
    for i in select:
        box2.delete(i)
 
 
def save_eng():
    f = open('eng_file.txt', 'w', encoding='utf-8-sig')
    f.writelines("\n".join(box2.get(0, END)))
    f.close()

def read_eng(): 
    with open('eng_file.txt', 'r', encoding='utf-8-sig') as file: 
        lst = file.readlines() 
    for item in lst:
        box2.insert(END, item)
 
 
 
root = Tk()
root.geometry('600x500')
 
box2 = Listbox(selectmode=EXTENDED)
box2.pack(side=LEFT)
scroll = Scrollbar(command=box2.yview)
scroll.pack(side=LEFT, fill=Y)
box2.config(yscrollcommand=scroll.set)
 
f = Frame()
f.pack(side=LEFT, padx=10)
tk.entry = Entry(f)
tk.entry.pack(anchor=N)


Button(f, text="add eng", command=add_eng)\
    .pack(fill=X)
Button(f, text="del eng", command=del_eng)\
    .pack(fill=X)
Button(f, text="save eng", command=save_eng)\
    .pack(fill=X)

Button(f, text="read eng", command=read_eng)\
    .pack(fill=X)



('---------------------------------------------------------------------------------') 
def add_rus():
    box1.insert(END, entry.get())
    entry.delete(0, END)
 
 
def del_rus():
    select = list(box1.curselection())
    select.reverse()
    for i in select:
        box1.delete(i)
 
 
def save_rus():
    s = open('rus.txt', 'w',  encoding='utf-8-sig')
    s.writelines("\n".join(box1.get(0, END)))
    s.close()

def read_rus(): 
    with open('rus_file.txt', 'r',  encoding='utf-8-sig') as file: 
        lst = file.readlines() 
    for item in lst:
        box1.insert(END, item)



box1 = Listbox(selectmode=EXTENDED)
box1.pack(side=RIGHT)
scroll = Scrollbar(command=box1.yview)
scroll.pack(side=RIGHT, fill=Y)
box1.config(yscrollcommand=scroll.set)

s = Frame()
s.pack(side=RIGHT, padx=10)
entry = Entry(s)
entry.pack(anchor=N)



Button(s, text="add rus", command=add_rus)\
    .pack(fill=X)
Button(s, text="del rus", command=del_rus)\
    .pack(fill=X)
Button(s, text="save rus", command=save_rus)\
    .pack(fill=X)

Button(s, text="read rus", command=read_rus)\
    .pack(fill=X)


('-----------------------------------------------------------------------------') 


 
root.mainloop()
