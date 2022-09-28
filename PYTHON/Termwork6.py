import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Simple Calculator")
root.geometry("600x400")

frame=ttk.Frame(root,padding="20 20 20 20")
frame.pack()

ttk.Label(frame, text="FirstNO:").grid(row=0,column=0,sticky=tk.E)
first=tk.StringVar()
ttk.Entry(frame,width=25,textvariable=first).grid(row=0,column=1)

ttk.Label(frame, text="SecondNO:").grid(row=1,column=0,sticky=tk.E)
second=tk.StringVar()
ttk.Entry(frame,width=25,textvariable=second).grid(row=1,column=1)
result=tk.StringVar()

def add():
    FirstNO = float(first.get())
    SecondNO = float(second.get())
    result.set(FirstNO+SecondNO)

def sub():
    FirstNO = float(first.get())
    SecondNO = float(second.get())
    result.set(FirstNO-SecondNO)

def mul():
    FirstNO = float(first.get())
    SecondNO = float(second.get())
    result.set(FirstNO*SecondNO)

def div():
    FirstNO = float(first.get())
    SecondNO = float(second.get())
    result.set(FirstNO/SecondNO)


ttk.Button(frame, text="ADD",command=add).grid(row=2,column=0)
ttk.Button(frame, text="SUB",command=sub).grid(row=2,column=1)
ttk.Button(frame, text="MUL",command=mul).grid(row=2,column=2)
ttk.Button(frame, text="DIV",command=div).grid(row=2,column=3)

ttk.Label(frame,text="RESULT").grid(row=3,column=0)
ttk.Entry(frame,width=25,textvariable=result,state="readonly").grid(row=3,column=1)

for child in frame.winfo_children():
    child.grid_configure(padx=10,pady=10)


root.mainloop()
