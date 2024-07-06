from tkinter import *
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()

root.geometry('925x500+700+200')
root.title("Get seats")
root.configure(bg = "gray")
root.resizable(False,False)

    
frame = Frame(root,width=3200,height=3500,bg='gray')
frame.place(x=0,y=0)

# commands..

#def cmd():
    
  #command1 = get_seats() 
  #command2 = book_seats()


def on_enter(e):
    seat.delete(0,'end')
def on_leave(e):
    name=seat.get()
    if name=='':
        seat.insert(0,'How many seats do you want to book.?')


# get seats...
#def get_seats():
 #import tkinter as tk
 #root = tk.Tk()
 #root.title("Movie Seat Selection")
 #root.geometry("925x500+700+200")

 #frame = Frame(root,width=3200,height=3500,bg='gray')
 #frame.place(x=0,y=0)

seat = Entry(frame,width = 25, fg="black",bg = "white", border = 2,font = ("Times new roman",11,"bold"))
seat.place(x = 30,y = 80)
seat.insert(0,"How many seats do you want to book.?")
seat.bind('<FocusIn>',on_enter)
seat.bind('<FocusOut>',on_leave)
 #root.destroy()
 #book_seats()




# booking seats...
def book_seats():
 import tkinter as tk
 root = tk.Tk()
 root.title("Movie Seat Selection")
 frame = Frame(root,width=3200,height=3500,bg='gray')
 frame.place(x=0,y=0)

  
 canvas = tk.Canvas(root, width=800, height=400)
 canvas.pack()

 seats = []
 for row in range(10):
     for col in range(10):
        seat = canvas.create_rectangle(col*40, row*40, col*40+30, row*40+30, fill="green")
        seats.append(seat)

 

 
   
 def toggle_seat(seat):
    root = tk.Tk()

    root.geometry('925x500+700+200')
    root.title("Ariyalur")
    
    frame = Frame(root,width=3200,height=3500,bg='gray')
    frame.place(x=0,y=0)

    Label(root,image=img,bg="gray").place(x = 0, y = 45)
    
    if canvas.itemcget(seat, "fill") == "green":
        canvas.itemconfig(seat,fill="red")
        #Button(root,width = 25, fg="black",bg = "white",text="Seat booked!!", border = 0,font = ("Times new roman",9,"bold"))
        #Button.place(x = 30,y = 30)
    else:
        canvas.itemconfig(seat, fill="green")
   
 for seat in seats:
    button = tk.Button(root, text="", command=lambda s=seat: toggle_seat(s))
    button.place(x=canvas.coords(seat)[0]+5, y=canvas.coords(seat)[1]+5)

root.mainloop()
