from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title("See The Time Now")
def time():
    s=strftime("%H:%M:%S %p")
    L.config(text=s)
    L.after(1000,time)

L=Label(root,font=("ds-digital",80),background="black",foreground="white")
L.pack(anchor="center")
time()
mainloop()

