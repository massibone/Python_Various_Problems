import tkinter
window = tkinter.Tk()
window.title("GUI")
label = tkinter.Label(window ,text = "Hello World!").pack()
window.mainloop()



from tkinter import *
window = Tk()
window.title("GUI")
label = Label(window ,text = "Hello World!").pack()
window.mainloop()

from tkinter import *
window = Tk()
window.title("GUI")
L1 = Label(window ,text="Hello!" ,font=("calibri" ,36 ,"bold"))
L1.grid(column=0 ,row=0)
window.mainloop()


from tkinter import *
window = Tk()
window.title("GUI")
window.geometry("500x500")
Bt = Button(window ,text="Enter" ,fg='red' ,bg='black')
Bt.place(x=250 ,y=250)
window.mainloop()

from tkinter import *
window = Tk()
window.title("GUI")
window.geometry("500x500")
def clicked():
    L1.configure(text = "Button was clicked!!")
L1 = Label()
L1.place(x=230 ,y=200)
Bt = Button(window ,text="Enter" ,command=clicked)
Bt.place(x=250 ,y=250)
window.mainloop()

from tkinter import *
window = Tk()
window.title("GUI")
window.geometry("300x300")
def clicked():
    l.configure(text = e.get())
e = Entry(window ,width=10)
l = Label(text="Text will pop-up here")
l.place(x=127 ,y=170)
e.place(x=130 ,y=140)
Bt = Button(window ,text="Enter" ,command=clicked)
Bt.place(x=130 ,y=100)
window.mainloop()

from tkinter import *
window = Tk()
window.title("GUI")
window.geometry("300x300")
Spin = Spinbox(window ,from_=0 ,to=10 ,width=5)
Spin.place(x=130 ,y=130)
window.mainloop()


from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("100x100")
messagebox.showinfo("information" ,"Information")
top.mainloop()


from Tkinter import *
import tkMessageBox
top = Tk()
Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Rust")
Lb1.insert(3, "C++")
Lb1.insert(4, "PHP")
Lb1.insert(5, "C#")
Lb1.insert(6, "Ruby")
Lb1.pack()
top.mainloop()

from Tkinter import *
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
    mylist.insert(END, "This is line number " + str(line))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
mainloop()


import tkinter
window = tkinter.Tk()
window.title("Welcome")
icon = tkinter.PhotoImage(file = "D:/testing downloads/image_2022-12-17_17-15-19.png")
label = tkinter.Label(window ,image = icon)
label.pack()
window.mainloop()


from tkinter import *
window = Tk()
window.title("Welcome")
window.geometry("200x200")
label = Label(text='Learning Python 101!')
label.place(x=70 ,y=20)
btn = Button(width=7 ,height=3)
def leftclick(event):
    label.configure(text="leftclick")
def middleclick(event):
    label.configure(text="middleclick")
def rightclick(event):
    label.configure(text="rightclick")

btn.bind("<Button-1>" ,leftclick)
btn.bind("<Button-2>" ,middleclick)
btn.bind("<Button-3>" ,rightclick)
btn.place(x=80 ,y=70)
window.mainloop()
