import tkinter as tk
from functools import partial
from tkinter import ttk

def findsum(l3, num1, num2):
    l3.config(state= "normal")
    n1 = int(num1.get())
    n2 = int(num2.get())
    n3 = n1 + n2
    l3.insert(tk.INSERT, str(n1+n2))


root = tk.Tk()
root.title("Calculator")
root.geometry("700x500")

number1 = tk.StringVar()
number2 = tk.StringVar()

result = tk.StringVar()

l1 = tk.Label(root, text="Enter 1st number").place(x=20, y=60)
l2 = tk.Label(root, text="Enter 2nd number").place(x=20, y=120)
l3 = tk.Label(root, text="Result:").place(x=20, y=180)

t1 = tk.Entry(root, textvariable=number1).place(x=200, y=60)
t2 = tk.Entry(root, textvariable=number2).place(x=200, y=120)

txtResult = tk.Entry(root)
txtResult.config(state= "disabled")
txtResult.place(x=200, y=180)


findsum = partial(findsum, txtResult, number1, number2)

b1 = tk.Button(root, text="ADD", command=findsum).place(x=200, y=300)
b2 = tk.Button(root, text="Cancel", command=root.destroy).place(x=250, y=300)

root.mainloop()
