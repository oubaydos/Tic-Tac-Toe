# cofing : utf-8
from tkinter import *
from tkinter import ttk
import tkinter.messagebox, time, winsound,msvcrt
global c
c=0
l=[]
root = Tk()
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='1.png')) #.subsample(5,5) dial tsghir tswira
root.title('tic  tac  toy')
root.geometry('355x260')
ttk.Style().configure("TButton",foreground="black",background='white')
def afterclick0():
    global c
    if c % 2==0:
        text = "X"
        l.append("x11")
    else:
        text = "O"
        l.append("011")
    btn.configure(text=text)
    c+=1
    print(c)
    print(l)

def afterclick1():
    global c
    if c % 2==0:
        text = "X"
        l.append("x12")
    else:
        text = "O"
        l.append("012")
    btn1.configure(text=text)
    c+=1
    print(c)
    print(l)


def afterclick2():
    global c
    if c % 2==0:
        text = "X"
        l.append("x13")
    else:
        text = "O"
        l.append("013")
    btn2.configure(text=text)
    c+=1
    print(c)
    print(l)


def afterclick3():
    global c
    if c % 2==0:
        text = "X"
        l.append("x21")
    else:
        text = "O"
        l.append("021")
    btn3.configure(text=text)
    c+=1
    print(c)
    print(l)


def afterclick4():
    global c
    if c % 2==0:
        text = "X"
        l.append("x22")
    else:
        text = "O"
        l.append("022")
    btn4.configure(text=text)
    c+=1
    print(c)
    print(l)


def afterclick5():
    global c
    if c % 2==0:
        text = "X"
        l.append("x23")
    else:
        text = "O"
        l.append("023")
    btn5.configure(text=text)
    c+=1
    print(c)
    print(l)


def afterclick6():
    global c
    if c % 2==0:
        text = "X"
        l.append("x31")
    else:
        text = "O"
        l.append("031")
    btn6.configure(text=text)
    c+=1
    print(c)
    print(l)


def afterclick7():
    global c
    if c % 2==0:
        text = "X"
        l.append("x32")
    else:
        text = "O"
        l.append("032")
    btn7.configure(text=text)
    c+=1
    print(c)
    print(l)


def afterclick8():
    global c
    if c % 2==0:
        text = "X"
        l.append("x33")
    else:
        text = "O"
        l.append("033")
    btn8.configure(text=text)
    c+=1
    print(c)
    print(l)



btn = ttk.Button(root,text='',command=afterclick0,style = 'W.TButton')
btn.grid(column=0,row=0,ipadx=20,ipady=20)
btn1 = ttk.Button(root,text='',command=afterclick1)
btn1.grid(column=0,row=1,ipadx=20,ipady=20)
btn2 = ttk.Button(root,text='',command=afterclick2)
btn2.grid(column=0,row=2,ipadx=20,ipady=20)
btn3 = ttk.Button(root,text='',command=afterclick3)
btn3.grid(column=1,row=0,ipadx=20,ipady=20)
btn4 = ttk.Button(root,text='',command=afterclick4)
btn4.grid(column=1,row=1,ipadx=20,ipady=20)
btn5 = ttk.Button(root,text='',command=afterclick5)
btn5.grid(column=1,row=2,ipadx=20,ipady=20)
btn6 = ttk.Button(root,text='',command=afterclick6)
btn6.grid(column=2,row=0,ipadx=20,ipady=20)
btn7 = ttk.Button(root,text='',command=afterclick7)
btn7.grid(column=2,row=1,ipadx=20,ipady=20)
btn8 = ttk.Button(root,text='',command=afterclick8)
btn8.grid(column=2,row=2,ipadx=20,ipady=20)


stp = ttk.Button(root,text='stop',command=root.destroy)
stp.grid(column=1,row=4,ipadx=20,ipady=20)



root.mainloop()

x1=["x11","x21","x31"]
x2=["x12","x22","x32"]
x3=["x13","x23","x33"]
x4=["x11","x12","x13"]
x5=["x21","x22","x23"]
x6=["x31","x32","x33"]
x7=["x31","x22","x13"]
x8=["x11","x22","x33"]


o1=["011","021","031"]
o2=["012","022","032"]
o3=["013","023","033"]
o4=["011","012","013"]
o5=["021","022","023"]
o6=["031","032","033"]
o7=["031","022","013"]
o8=["011","022","033"]


x=[x1,x2,x3,x4,x5,x6,x7,x8,'']
o=[o1,o2,o3,o4,o5,o6,o7,o8,'']
c1=0
c2=0
def h():
    c1=0
    for j in range(len(x)-1):
     for i in x[j]:
      if i in l:
        c1+=1
     if c1==3:
         return "player 1"
     else :
        c1=0
def h1():
    c2=0
    for j in range(len(o)-1):
     for i in o[j]:
      if i in l:
        c2+=1
     if c2==3:
        return "player 2"
     else :
        c2=0
print(h())
print(h1())
if h()!="player 1" and h1()!="player 2":
    print("draw")

def kk():
    if h()!=None:
        return h()
    elif h1()!=None:
        return h1()
    else:
        return "draw"
def res():
    if kk()==h() or kk()==h1():
        return "congrats, " + kk() + " is the winner"
    elif kk()=="draw":
        return kk()
resultat = Tk()
resultat.title('resultat')
resultat.geometry('455x70')
label =Label(resultat,text=res(),font=("Arial Bold",25),fg=('orange'))# new label + text  + font + font size

label.grid(column=0, row=0)

"""new = ttk.Button(resultat,text='stop',command=Toplevel(root))
new.grid(column=1,row=4,ipadx=20,ipady=20)"""
resultat.mainloop()

