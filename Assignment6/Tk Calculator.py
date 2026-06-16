from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("300x400")
# def(
def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))
    

# entry()
e=Entry(root,width=52,borderwidth=6,font=("Arial",18))
e.place(x=0,y=0)
b=Button(text="1",width=10,command=lambda:click(1))
b.place(x=10,y=60)
b=Button(text="2",width=10,command=lambda:click(2))
b.place(x=60,y=60)
b=Button(text="3",width=10,command=lambda:click(3))
b.place(x=110,y=60)
b=Button(text="4",width=10,command=lambda:click(4))
b.place(x=10,y=120)
b=Button(text="5",width=10,command=lambda:click(5))
b.place(x=60,y=120)
b=Button(text="6",width=10,command=lambda:click(6))
b.place(x=110,y=120)
b=Button(text="7",width=10,command=lambda:click(7))
b.place(x=10,y=180)
b=Button(text="8",width=10,command=lambda:click(8))
b.place(x=60,y=180)
b=Button(text="9",width=10,command=lambda:click(9))
b.place(x=110,y=180)
b=Button(text="0",width=10,command=lambda:click(0))
b.place(x=10,y=240)
# # operation
def add():
    n1=e.get()
    global i
    i=int(n1)
    global math 
    math="add"
    e.delete(0,END)
def sub():
    n1=e.get()
    global i
    i=int(n1)
    global math 
    math="sub"
    e.delete(0,END)
def mul():
    n1=e.get()
    global i
    i=int(n1)
    global math 
    math="mul"
    e.delete(0,END)
def div():
    n1=e.get()
    global i
    i=int(n1)
    global math 
    math="div"
    e.delete(0,END)
def equal():
    n2=e.get()
    e.delete(0,END)
    if(math=="add"):
        e.insert(0,i+int(n2))
    elif(math=="sub"):
        e.insert(0 ,i-int(n2))
    elif (math=="mul"):
        e.insert(0 ,i*int(n2))
    elif(math=="div"):
        e.insert(0,i/int(n2))
def clear():
    e.delete(0,END)
          
b=Button(text="+",width=10,command=add)
b.place(x=60,y=240)
b=Button(text="-",width=10,command=sub)
b.place(x=110,y=240)
b=Button(text="*",width=10,command=mul)
b.place(x=10,y=300)
b=Button(text="/",width=10,command=div)
b.place(x=60,y=300)
b=Button(text="=",width=10,command=equal)
b.place(x=110,y=300)
b=Button(text="clr",width=10,command=clear)
b.place(x=200,y=60)


root.mainloop()