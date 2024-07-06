#thanjavur
#Thanjavur
from tkinter import *
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()

root.geometry('925x500+700+200')
root.title("Thanjavur")
    
frame = Frame(root,width=3200,height=3500,bg='gray')
frame.place(x=0,y=0)

img=PhotoImage(file="C:\ADITYA.G\PYTHON FILES\home.png",height=1500,width=1000)
Label(root,image=img,bg="gray").place(x = 0, y = 45)


def display_cities():
  for city in cities:
    label = tk.Label(root,text=city,bg="gray")
    label.pack()

def theatre1():
  messagebox.askyesno("Information","Select Thanjavur theatres.?")
  root.destroy()
  Thanjavur_theatres()

def Abirami_films():
 root = Tk()
 root.geometry('925x500+700+200')
 root.title("Abirami")

 frame = Frame(root,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)

 messagebox.showinfo("Information","Selectd Abirami theatres")
 root.destroy()
 Abirami_films1()


def Abirami_films1():
 win = Tk()
 win.geometry('925x500+700+200')
 win.title("Abirami")

 frame = Frame(win,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)

########################################-------------------------------
 
 s_films=[]
 sm1 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Transformers-the rise of beasts",font = ("Times sangeetha roman",11,"bold")).place(x = 50,y = 50)
 s_films.append(sm1)
 sm2 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Horrors of the heart",font = ("Times sangeetha roman",11,"bold")).place(x = 50,y = 90)
 s_films.append(sm2)
 #root.destroy()
 
def display_cities():
    for city in s_films:
       label = tk.Label(root,text=city,bg="gray")
       label.pack()


def jothi_films():
 root = Tk()
 root.geometry('925x500+700+200')
 root.title("jothi")

 frame = Frame(root,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)

 messagebox.showinfo("Information","Selectd sangeetha cinema theatres")
 root.destroy()
 jothi_films1()


def jothi_films1():
 win = Tk()
 win.geometry('925x500+700+200')
 win.title("jothi")

 frame = Frame(win,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)

  
 st_films=[]
 st1 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="The Thalainagaram-2",font = ("Times sangeetha roman",11,"bold")).place(x = 50,y = 50)
 st_films.append(st1)
 st2 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Asvins",font = ("Times sangeetha roman",11,"bold")).place(x = 50,y = 90)
 st_films.append(st2)
 #root.destroy()
 
def display_cities():
    for city in st_films:
       label = tk.Label(root,text=city,bg="gray")
       label.pack()

###########################################---------------------------------------------------


 
j_films=[]
jm1 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "blue", border = 0,text="Spiderman-across the spiderverse",font = ("Times sangeetha roman",11,"bold")).place(x = 50,y = 50)
j_films.append(jm1)
jm2 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "yellow", border = 0,text="Elemental",font = ("Times sangeetha roman",11,"bold")).place(x = 50,y = 90)
j_films.append(jm2)
 #root.destroy()
 
def display_cities():
    for city in j_films:
       label = tk.Label(root,text=city,bg="gray")
       label.pack()


def gk_cinemas_films():
 root = Tk()
 root.geometry('925x500+700+200')
 root.title("gk_cinemas")

 frame = Frame(root,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)

 messagebox.showinfo("Information","Selectd gk_cinemas theatres")
 root.destroy()
 gk_cinemas_films1()


def gk_cinemas_films1():
 win = Tk()
 win.geometry('925x500+700+200')
 win.title("gk_cinemas")

 frame = Frame(win,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)

  
 jt_films=[]
 jt1 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Spiderman-across the spiderverse",font = ("Times sangeetha roman",11,"bold")).place(x = 50,y = 50)
 jt_films.append(jt1)
 jt2 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Elemental",font = ("Times sangeetha roman",11,"bold")).place(x = 50,y = 90)
 jt_films.append(jt2)
 #root.destroy()
 
def display_cities():
    for city in jt_films:
       label = tk.Label(root,text=city,bg="gray")
       label.pack()






###########################################_________________________________________________________
def Thanjavur_theatres():
 root = Tk()
 root.geometry('925x500+700+200')
 root.title("Thanjavur")
    
 frame = Frame(root,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)
 at1 = Label(frame,width = 100, fg="black",bg = "sky blue", border = 4,text="Theatres available in Thanjavur..!",font = ("Times sangeetha roman",11,"bold"))
 at1.place(x = 40,y = 12)

 l1 = Label(frame,width = 5, fg="white",bg = "black", border = 2,text="> T1",font = ("Times sangeetha roman",11,"bold"))
 l1.place(x = 50,y = 75)
 l2 = Label(frame,width = 5, fg="white",bg = "black", border = 2,text="> T2",font = ("Times sangeetha roman",11,"bold"))
 l2.place(x = 50,y = 115)
# l3 = Label(frame,width = 5, fg="white",bg = "black", border = 2,text="> T3",font = ("Times sangeetha roman",11,"bold"))
 #l3.place(x = 50,y = 155)

 theatres = []
 t1=Button(frame,height=0,width = 65,pady=2,text='Abirami theatre',bg='red',command=Abirami_films,font=('Times sangeetha Roman',10,'bold'),fg='white',border=0).place(x=100,y=75)
 theatres.append(t1)
 t2=Button(frame,height=0,width = 65,pady=2,text='sangeetha cinema',bg='red',command = jothi_films,font=('Times sangeetha Roman',10,'bold'),fg='white',border=0).place(x=100,y=115)
 theatres.append(t2)
 #t3=Button(frame,height=0,width = 65,pady=2,text='gk_cinemas theatre',bg='red',command = gk_cinemas_films,font=('Times sangeetha Roman',10,'bold'),fg='white',border=0).place(x=100,y=155)
 #theatres.append(t3)

def display_cities():
    for city in theatres:
       label = tk.Label(root,text=city,bg="gray")
       label.pack()





           
s = Label(frame,width = 65, fg="black",bg = "white", border = 4,text=">>>>> Select theatres in Thanjavur..! <<<<<",font = ("Times sangeetha roman",11,"bold"))
s.place(x = 40,y = 12)
Button(frame,height=0,width = 20,pady=4,text='View theatres ↓',bg='red',command =theatre1 ,font=('Times sangeetha Roman',10,'bold'),fg='white',border=2.0).place(x=640,y=10)




