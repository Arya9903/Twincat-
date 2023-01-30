from tkinter import *
import pyads
import time
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
# connect to plc and open connection
plc = pyads.Connection('172.18.238.139.1.1', 851)
plc.open()
#plt.axis([41000, 42000, -125, 260])
# read int value by name
#plc.read_by_name("k")
global lastdata
lastdata=[]
x=[]
y=[]
ll=[]
t=count()
#data= plc.read_by_name("GVL.b[1]"
def dataupdate():
    global data
    data= plc.read_by_name("GVL.b[1]")
    x.append(next(t))
    y.append(data)
def live(i):
    dataupdate()
    plt.plot(x,y)
    print(data)
#print(x)
#print(y)
k=0
def update():
    global k
    dataupdate()
    lastdata.append(data)
    label=Label(root,text=data,font=("Times New Roman",25),fg="black")
    label.pack()
    ll.append(label)
    print(f" len ll is  {len(ll)}")
    ll[len(ll)-2].pack_forget()
    #print(ll)
    #print(lastdata)
    #print(k)
    k+=1
    root.after(500,update)
def plott():
    a=FuncAnimation(plt.gcf(),live,interval=50)
    plt.tight_layout()
    plt.show()
root=Tk()
label=Label(root,text="Value",font=("Times New Roman",25), fg="black").pack()
root.geometry("200x150")
root.title("Tracking System")
root.after(1000,update)
root.after(1000,plott)
root.mainloop()
"""
print(x)
plt.plot(y,x)

plt.show()
plc.close()
"""
