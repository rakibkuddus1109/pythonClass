# importing required libraries

import tkinter
from tkinter import *

root = tkinter.Tk()

root.geometry("500x400+100+200")
root.resizable(0,0)
root.title("Calculator")

data = StringVar()

lbl = Label(root,text = "Label Page",font=("Verdana",22),anchor=SE,textvariable=data)
lbl.pack(expand=True,fill="both")

val = ""

def btn1_clicked():
    global val
    val = val + "1"
    data.set(val)

def btn2_clicked():
    global val
    val = val + "2"
    data.set(val)

def btn3_clicked():
    global val
    val = val + "3"
    data.set(val)

def btn4_clicked():
    global val
    val = val + "4"
    data.set(val)

def btn5_clicked():
    global val
    val = val + "5"
    data.set(val)

def btn6_clicked():
    global val
    val = val + "6"
    data.set(val)

def btn7_clicked():
    global val
    val = val + "7"
    data.set(val)

def btn8_clicked():
    global val
    val = val + "8"
    data.set(val)

def btn9_clicked():
    global val
    val = val + "9"
    data.set(val)

def btn0_clicked():
    global val
    val = val + "0"
    data.set(val)

def btnadd_clicked():
    global val
    val = val + "+"
    data.set(val)

def btnsub_clicked():
    global val
    val = val + "-"
    data.set(val)

def btnmul_clicked():
    global val
    val = val + "*"
    data.set(val)

def btndiv_clicked():
    global val
    val = val + "/"
    data.set(val)

def btnclr_clicked():
    global val
    val = ""
    data.set(val)

def btneql_clicked():
    global val
    val = str(eval(val))
    data.set(val)

frame1 = Frame(root)
frame1.pack(expand=True,fill="both")

frame2 = Frame(root)
frame2.pack(expand=True,fill="both")

frame3 = Frame(root)
frame3.pack(expand=True,fill="both")

frame4 = Frame(root)
frame4.pack(expand=True,fill="both")

# frame1 button

btn1 = Button(frame1,bg="white",text="1",font=("Verdana",22),border=0,command=btn1_clicked)
btn1.pack(expand=True,fill="both",side=LEFT)

btn2 = Button(frame1,bg="white",text="2",font=("Verdana",22),border=0,command=btn2_clicked)
btn2.pack(expand=True,fill="both",side=LEFT)

btn3 = Button(frame1,bg="white",text="3",font=("Verdana",22),border=0,command=btn3_clicked)
btn3.pack(expand=True,fill="both",side=LEFT)

btn4 = Button(frame1,bg="white",text="+",font=("Verdana",22),border=0,command=btnadd_clicked)
btn4.pack(expand=True,fill="both",side=LEFT)

# frame2 button

btn5 = Button(frame2,bg="white",text="4",font=("Verdana",22),border=0,command=btn4_clicked)
btn5.pack(expand=True,fill="both",side=LEFT)

btn6 = Button(frame2,bg="white",text="5",font=("Verdana",22),border=0,command=btn5_clicked)
btn6.pack(expand=True,fill="both",side=LEFT)

btn7 = Button(frame2,bg="white",text="6",font=("Verdana",22),border=0,command=btn6_clicked)
btn7.pack(expand=True,fill="both",side=LEFT)

btn8 = Button(frame2,bg="white",text="-",font=("Verdana",22),border=0,command=btnsub_clicked)
btn8.pack(expand=True,fill="both",side=LEFT)

# frame3 button

btn9 = Button(frame3,bg="white",text="7",font=("Verdana",22),border=0,command=btn7_clicked)
btn9.pack(expand=True,fill="both",side=LEFT)

btn10 = Button(frame3,bg="white",text="8",font=("Verdana",22),border=0,command=btn8_clicked)
btn10.pack(expand=True,fill="both",side=LEFT)

btn11 = Button(frame3,bg="white",text="9",font=("Verdana",22),border=0,command=btn9_clicked)
btn11.pack(expand=True,fill="both",side=LEFT)

btn12 = Button(frame3,bg="white",text="*",font=("Verdana",22),border=0,command=btnmul_clicked)
btn12.pack(expand=True,fill="both",side=LEFT)

# frame4 button

btn13 = Button(frame4,bg="white",text="0",font=("Verdana",22),border=0,command=btn0_clicked)
btn13.pack(expand=True,fill="both",side=LEFT)

btn14 = Button(frame4,bg="white",text="C",font=("Verdana",22),border=0,command=btnclr_clicked)
btn14.pack(expand=True,fill="both",side=LEFT)

btn15 = Button(frame4,bg="white",text="=",font=("Verdana",22),border=0,command=btneql_clicked)
btn15.pack(expand=True,fill="both",side=LEFT)

btn16 = Button(frame4,bg="white",text="/",font=("Verdana",22),border=0,command=btndiv_clicked)
btn16.pack(expand=True,fill="both",side=LEFT)

root.mainloop()