from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import tkinter as tk
from tkVideoPlayer import TkinterVideo

root = tk.Tk()

root.geometry('200x200')
root.title("Coimbatore")
root.configure(bg = "gray")
root.resizable(False,False)

    
frame = Frame(root,width=3200,height=3500,bg='black')
frame.place(x=0,y=0)

def theatre1():
  root.destroy()
  import city3_coimbatore_theatres

import graph           
Button(frame,height=0,width = 20,pady=4,text='View theatres ↓',bg='red',command =theatre1 ,font=('Times New Roman',10,'bold'),fg='white',border=2.0).place(x=20,y=60)
