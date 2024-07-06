#Sivagangai
#Sivagangai
from tkinter import *
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()

root.geometry('925x500+700+200')
root.title("Sivagangai")
    
frame = Frame(root,width=3200,height=3500,bg='gray')
frame.place(x=0,y=0)

img=PhotoImage(file="C:\ADITYA.G\PYTHON FILES\home.png",height=1500,width=1000)
Label(root,image=img,bg="gray").place(x = 0, y = 45)


def display_cities():
  for city in cities:
    label = tk.Label(root,text=city,bg="gray")
    label.pack()

def theatre1():
  messagebox.askyesno("Information","Select Sivagangai theatres.?")
  root.destroy()
  Sivagangai_theatres()

def Srk_films():
 root = Tk()
 root.geometry('925x500+700+200')
 root.title("Srk")

 frame = Frame(root,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)

 messagebox.showinfo("Information","Selectd Srk theatres")
 root.destroy()
 Srk_films1()


def Srk_films1():
 win = Tk()
 win.geometry('925x500+700+200')
 win.title("Srk")

 frame = Frame(win,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)

########################################-------------------------------
 
 s_films=[]
 sm1 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Regina",font = ("Times new roman",11,"bold")).place(x = 50,y = 50)
 s_films.append(sm1)
 sm2 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Transformer- the rise of the beasts",font = ("Times new roman",11,"bold")).place(x = 50,y = 90)
 s_films.append(sm2)
 #root.destroy()
 
def display_cities():
    for city in s_films:
       label = tk.Label(root,text=city,bg="gray")
       label.pack()


def Shanthi_films():
 root = Tk()
 root.geometry('925x500+700+200')
 root.title("Shanthi")

 frame = Frame(root,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)

 messagebox.showinfo("Information","Selectd Shanthi theatres")
 root.destroy()
 Shanthi_films1()


def Shanthi_films1():
 win = Tk()
 win.geometry('925x500+700+200')
 win.title("Shanthi")

 frame = Frame(win,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)

  
 st_films=[]
 st1 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="The Flash",font = ("Times new roman",11,"bold")).place(x = 50,y = 50)
 st_films.append(st1)
 st2 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Regina",font = ("Times new roman",11,"bold")).place(x = 50,y = 90)
 st_films.append(st2)
 #root.destroy()
 
def display_cities():
    for city in st_films:
       label = tk.Label(root,text=city,bg="gray")
       label.pack()

###########################################---------------------------------------------------


 
j_films=[]
jm1 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "blue", border = 0,text="Spiderman-across the spiderverse",font = ("Times new roman",11,"bold")).place(x = 50,y = 50)
j_films.append(jm1)
jm2 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "yellow", border = 0,text="Transformer- the rise of the beasts",font = ("Times new roman",11,"bold")).place(x = 50,y = 90)
j_films.append(jm2)
 #root.destroy()
 
def display_cities():
    for city in j_films:
       label = tk.Label(root,text=city,bg="gray")
       label.pack()


def Vijay_films():
 root = Tk()
 root.geometry('925x500+700+200')
 root.title("Vijay")

 frame = Frame(root,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)

 messagebox.showinfo("Information","Selectd Vijay theatres")
 root.destroy()
 Vijay_films1()


def Vijay_films1():
 win = Tk()
 win.geometry('925x500+700+200')
 win.title("Vijay")

 frame = Frame(win,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)

  
 jt_films=[]
 jt1 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Spiderman-across the spiderverse",font = ("Times new roman",11,"bold")).place(x = 50,y = 50)
 jt_films.append(jt1)
 jt2 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Transformer- the rise of the beasts",font = ("Times new roman",11,"bold")).place(x = 50,y = 90)
 jt_films.append(jt2)
 #root.destroy()
 
def display_cities():
    for city in jt_films:
       label = tk.Label(root,text=city,bg="gray")
       label.pack()






###########################################_________________________________________________________
def Sivagangai_theatres():
 root = Tk()
 root.geometry('925x500+700+200')
 root.title("Sivagangai")
    
 frame = Frame(root,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)
 at1 = Label(frame,width = 100, fg="black",bg = "sky blue", border = 4,text="Theatres available in Sivagangai..!",font = ("Times new roman",11,"bold"))
 at1.place(x = 40,y = 12)

 l1 = Label(frame,width = 5, fg="white",bg = "black", border = 2,text="> T1",font = ("Times new roman",11,"bold"))
 l1.place(x = 50,y = 75)
 l2 = Label(frame,width = 5, fg="white",bg = "black", border = 2,text="> T2",font = ("Times new roman",11,"bold"))
 l2.place(x = 50,y = 115)
 l3 = Label(frame,width = 5, fg="white",bg = "black", border = 2,text="> T3",font = ("Times new roman",11,"bold"))
 l3.place(x = 50,y = 155)

 theatres = []
 t1=Button(frame,height=0,width = 65,pady=2,text='Srk theatre',bg='red',command=Srk_films,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=100,y=75)
 theatres.append(t1)
 t2=Button(frame,height=0,width = 65,pady=2,text='Shanthi max',bg='red',command = Shanthi_films,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=100,y=115)
 theatres.append(t2)
 t3=Button(frame,height=0,width = 65,pady=2,text='Vijay theatre',bg='red',command = Vijay_films,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=100,y=155)
 theatres.append(t3)

def display_cities():
    for city in theatres:
       label = tk.Label(root,text=city,bg="gray")
       label.pack()





           
s = Label(frame,width = 65, fg="black",bg = "white", border = 4,text=">>>>> Select theatres in Sivagangai..! <<<<<",font = ("Times new roman",11,"bold"))
s.place(x = 40,y = 12)
Button(frame,height=0,width = 20,pady=4,text='View theatres ↓',bg='red',command =theatre1 ,font=('Times New Roman',10,'bold'),fg='white',border=2.0).place(x=640,y=10)









