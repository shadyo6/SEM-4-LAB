from tkinter import *

class Calculator:
    def __init__(self,root):
        self.lbl1 = Label(root,text="Enter 1st side: ",fg="blue",font = (16))
        self.lbl1.grid(row = 1 ,column = 1,padx=25,pady = 25)

        self.txtEntry1 = Entry(root)
        self.txtEntry1.grid(row = 1 ,column = 2,padx=25,pady = 25)

        self.lbl2 = Label(root,text="Enter 2nd side: ",fg="blue",font = (16))
        self.lbl2.grid(row = 2 ,column = 1)

        self.txtEntry2 = Entry(root)
        self.txtEntry2.grid(row = 2 ,column = 2,padx=25,pady = 25)

        self.lbl3 = Label(root,text="Result: ",fg="blue",font = (16))
        self.lbl3.grid(row = 3 ,column = 1,padx=25,pady = 25)

        self.txtEntry3 = Entry(root)
        self.txtEntry3.grid(row = 3 ,column = 2,padx=25,pady = 25)
        self.txtEntry3.config(state= "disabled")

        self.btnAdd = Button(root,text="Calculate",command = self.CalcArea,font=("arial",12,"bold"),bg="light blue")
        self.btnAdd.grid(row=4,column = 0, columnspan = 3,padx=25,pady = 25)
    def CalcArea(self):
        self.txtEntry3.config(state = "normal")
        self.txtEntry3.delete(0,END)
        num1= int(self.txtEntry1.get())
        num2= int(self.txtEntry2.get())
        self.txtEntry3.insert(END, str(num1+num2))
        self.txtEntry3.config(state = "disabled")

root = Tk()
root.title("Calculator")
root.geometry("400x400")
trObj = Calculator(root)
root.mainloop()