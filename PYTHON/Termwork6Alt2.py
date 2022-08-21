from tkinter import *

class MyCalc:
    def __init__(self,root):
        frame1 = Frame(root,bg="yellow")
        frame1.pack(fill=X)

        self.lbl1 = Label(frame1,text="Enter 1st num: ",fg="blue",bg = "yellow", font = (16))
        self.lbl1.pack(side = LEFT, padx=25, pady=25)

        self.tbox1 = Entry(frame1,font=("arial",12,"bold"),bg="white")
        self.tbox1.pack(side = LEFT, padx=25, pady=25)

        frame2 = Frame(root)
        frame2.pack(fill=X)

        self.lbl2 = Label(frame2,text="Enter 2nd num: ",fg="blue",bg = "yellow",font = (16))
        self.lbl2.pack(side = LEFT, padx=25, pady=25)

        self.tbox2 = Entry(frame2,font=("arial",12,"bold"),bg="white")
        self.tbox2.pack(side = LEFT, padx=25, pady=25)

        frame3 = Frame(root)
        frame3.pack(fill=X)
        self.lbl3 = Label(frame3,text="Result is:           ",fg="blue",bg = "yellow",font = (16))
        self.lbl3.pack(side = LEFT, padx=25, pady=25)
        self.tbox3 = Entry(frame3,font=("arial",12,"bold"),bg="white")
        self.tbox3.pack(side = LEFT, padx=25, pady=25)

        frame4 = Frame(root)
        frame4.pack(fill=BOTH)
        self.btnAdd = Button(frame4,text="Sum",command = self.Add,font=("arial",12,"bold"),bg="light blue")
        self.btnAdd.pack(side = LEFT, padx=25, pady=20)

        self.btnAdd = Button(frame4,text="Diff",command = self.Diff,font=("arial",12,"bold"),bg="light blue")
        self.btnAdd.pack(side = LEFT, padx=25, pady=20)

        self.btnProd = Button(frame4,text="Prod",command = self.Prod,font=("arial",12,"bold"),bg="light blue")
        self.btnProd.pack(side = LEFT, padx=25, pady=20)

        self.btnProd = Button(frame4,text="Div",command = self.Div,font=("arial",12,"bold"),bg="light blue")
        self.btnProd.pack(side = LEFT, padx=25, pady=20)

    def Add(self):
        self.tbox3.delete(0,END)
        num1= int(self.tbox1.get())
        num2= int(self.tbox2.get())
        self.tbox3.insert(END, str(num1+num2))

    def Diff(self):
        self.tbox3.delete(0,END)
        num1= int(self.tbox1.get())
        num2= int(self.tbox2.get())
        self.tbox3.insert(END, str(num1- num2))

    def Prod(self):
        self.tbox3.delete(0,END)
        num1= int(self.tbox1.get())
        num2= int(self.tbox2.get())
        self.tbox3.insert(END, str(num1* num2))

    def Div(self):
        self.tbox3.delete(0,END)
        num1= int(self.tbox1.get())
        num2= int(self.tbox2.get())
        self.tbox3.insert(END, str(num1/ num2))


def main():
    root = Tk()
    root.title("Calculator")
    root.geometry("400x400")
    root.config(bg="white")
    myCalc = MyCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
