from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk

root = tk.Tk()
root.geometry('602x505+100+100')
root.title("Coimbatore")
root.configure(bg="gray")
root.resizable(False, False)

frame = Frame(root, width=600, height=500, bg='gray')
frame.place(x=0, y=0)

#img=PhotoImage(file="C:\ADITYA.G\PYTHON FILES\Select theatre.png",height=1500,width=1000)
#Label(root,image=img,bg="gray").place(x = 0, y = 45)

################################## SEAT BOOKING FOR TH1 M1 ##############################################

def get_seats_th1_a():
 import tkinter as tk
 root = tk.Tk()
 root.geometry("525x350")
 root.configure(bg = "gray")
 root.resizable(False,False)
 root.title("Seat credentials")

 frame = Frame(root,width=1200,height=1500,bg='gray')
 frame.place(x=0,y=0)

 def on_enter(e):
    seat.delete(0,'end')
 def on_leave(e):
    name=seat.get()
    if name=='':
        seat.insert(0,'How many seats do you want to book.?')
 seat = Entry(frame,width = 40, fg="black",bg = "white", border = 4,font = ("Times new roman",11,"bold"))
 seat.place(x = 50,y = 14)
 seat.insert(0,"How many seats do you want to book.?")
 seat.bind('<FocusIn>',on_enter)
 seat.bind('<FocusOut>',on_leave)

 def entry_th1_a():
    enter_text = seat.get()
    try:
        num_seats = int(enter_text)
        if num_seats > 0:
            book_seats_th1_a()
        else:
            messagebox.showerror("Invalid", "Enter a valid input")
    except ValueError:
        messagebox.showerror("Invalid", "Enter a valid input")

 Button(frame, height=0, width=15, pady=4, text='Enter ↓', bg='red', command=entry_th1_a,font=('Times New Roman', 10, 'bold'), fg='white', border=2.0).place(x=150, y=93)

 def show_selected_time():
   global selected_time
   selected_time = time_var.get()
   selected_time
   
 time_var = tk.StringVar(root)
 time_var.set("Select a show time")

 time_option_menu = tk.OptionMenu(root, time_var, "10:00 AM", "2:00 PM", "6:00 PM", "9:00 PM", "11:00 PM")
 time_option_menu.place(x=110,y=45)
 
 show_button = tk.Button(root, text="OK", command=show_selected_time)
 show_button.place(x=260,y=50)

 root.mainloop() 

######################################################################################



def display_booking_details_th1_a(movie_name, num_seats, show_time, theater):
    messagebox.showinfo("Ticket Booked", f"Movie: {movie_name}\nNumber of Seats: {num_seats}\nShow Time: {show_time}\nTheater: {theater}")



def book_seats_th1_a():
    root = tk.Tk()
    root.title("Movie Seat Selection")

    canvas = tk.Canvas(root, width=1000, height=500)
    canvas.pack()

    seats = []
    for row in range(12):
        for col in range(13):
            seat = canvas.create_rectangle(col*40, row*40, col*40+30, row*40+30, fill="green")
            seats.append(seat)

    # Add movie screen
    screen = canvas.create_rectangle(00, 480, 530, 600, fill="black")

    def toggle_seat_th1_a(seat):
        if canvas.itemcget(seat, "fill") == "green":
            canvas.itemconfig(seat, fill="red")
        else:
            canvas.itemconfig(seat, fill="green")
            
            
    def confirm_booking_th1_a():
        selected_seats = []
        for seat in seats:
            if canvas.itemcget(seat, "fill") == "red":
                selected_seats.append(seat)

        if len(selected_seats) > 0:
            num_seats = len(selected_seats)
            movie_name = "Transformers-Rise of the beasts"  # Replace with the actual movie name
            show_time = f"{selected_time}"  # Replace with the actual show time
            theater = "Cinepolis theatre"  # Replace with the actual theater name

            display_booking_details_th1_a(movie_name, num_seats, show_time, theater)
        else:
            messagebox.showerror("Error", "No seats selected!")

    for seat in seats:
        button = tk.Button(root, text="", command=lambda s=seat: toggle_seat_th1_a(s))
        button.place(x=canvas.coords(seat)[0]+5, y=canvas.coords(seat)[1]+5)

    screen_label = Label(root, text=" <<<<<<<<  This side screen  >>>>>>>> ",fg = "white",bg = "black",font = ("times new roman",12,"bold"))
    canvas.create_window(285, 490, window = screen_label)
       
      
    confirm_button = tk.Button(root, text="Confirm Booking",bg = "red",fg="white", command=confirm_booking_th1_a)
    confirm_button.pack()

    root.mainloop()
    #root.destroy()
    
#############################################################################################################################

################################## SEAT BOOKING FOR TH1 M2 ##############################################

def get_seats_th1_b():
 import tkinter as tk
 root = tk.Tk()
 root.geometry("525x350")
 root.configure(bg = "gray")
 root.resizable(False,False)
 root.title("Seat credentials")

 frame = Frame(root,width=1200,height=1500,bg='gray')
 frame.place(x=0,y=0)

 def on_enter(e):
    seat.delete(0,'end')
 def on_leave(e):
    name=seat.get()
    if name=='':
        seat.insert(0,'How many seats do you want to book.?')
 seat = Entry(frame,width = 40, fg="black",bg = "white", border = 4,font = ("Times new roman",11,"bold"))
 seat.place(x = 50,y = 14)
 seat.insert(0,"How many seats do you want to book.?")
 seat.bind('<FocusIn>',on_enter)
 seat.bind('<FocusOut>',on_leave)

 def entry_th1_b():
    enter_text = seat.get()
    try:
        num_seats = int(enter_text)
        if num_seats > 0:
            book_seats_th1_b()
        else:
            messagebox.showerror("Invalid", "Enter a valid input")
    except ValueError:
        messagebox.showerror("Invalid", "Enter a valid input")

 Button(frame, height=0, width=15, pady=4, text='Enter ↓', bg='red', command=entry_th1_b,font=('Times New Roman', 10, 'bold'), fg='white', border=2.0).place(x=150, y=93)

 def show_selected_time():
   global selected_time
   selected_time = time_var.get()
   selected_time
   
 time_var = tk.StringVar(root)
 time_var.set("Select a show time")

 time_option_menu = tk.OptionMenu(root, time_var, "10:00 AM", "2:00 PM", "6:00 PM", "9:00 PM", "11:00 PM")
 time_option_menu.place(x=110,y=45)
 
 show_button = tk.Button(root, text="OK", command=show_selected_time)
 show_button.place(x=260,y=50)

 root.mainloop() 

######################################################################################



def display_booking_details_th1_b(movie_name, num_seats, show_time, theater):
    messagebox.showinfo("Ticket Booked", f"Movie: {movie_name}\nNumber of Seats: {num_seats}\nShow Time: {show_time}\nTheater: {theater}")



def book_seats_th1_b():
    root = tk.Tk()
    root.title("Movie Seat Selection")

    canvas = tk.Canvas(root, width=1000, height=500)
    canvas.pack()

    seats = []
    for row in range(12):
        for col in range(13):
            seat = canvas.create_rectangle(col*40, row*40, col*40+30, row*40+30, fill="green")
            seats.append(seat)

    # Add movie screen
    screen = canvas.create_rectangle(00, 480, 530, 600, fill="black")

    def toggle_seat_th1_b(seat):
        if canvas.itemcget(seat, "fill") == "green":
            canvas.itemconfig(seat, fill="red")
        else:
            canvas.itemconfig(seat, fill="green")
            
            
    def confirm_booking_th1_b():
        selected_seats = []
        for seat in seats:
            if canvas.itemcget(seat, "fill") == "red":
                selected_seats.append(seat)

        if len(selected_seats) > 0:
            num_seats = len(selected_seats)
            movie_name = "Por thozhil"  # Replace with the actual movie name
            show_time = f"{selected_time}"  # Replace with the actual show time
            theater = "Cinepolis theatre"  # Replace with the actual theater name

            display_booking_details_th1_b(movie_name, num_seats, show_time, theater)
        else:
            messagebox.showerror("Error", "No seats selected!")

    for seat in seats:
        button = tk.Button(root, text="", command=lambda s=seat: toggle_seat_th1_b(s))
        button.place(x=canvas.coords(seat)[0]+5, y=canvas.coords(seat)[1]+5)

    screen_label = Label(root, text=" <<<<<<<<  This side screen  >>>>>>>> ",fg = "white",bg = "black",font = ("times new roman",12,"bold"))
    canvas.create_window(285, 490, window = screen_label)
       
      
    confirm_button = tk.Button(root, text="Confirm Booking",bg = "red",fg="white", command=confirm_booking_th1_b)
    confirm_button.pack()

    root.mainloop()
    #root.destroy()
    
#############################################################################################################################


################################## SEAT BOOKING FOR TH2 M1 ##############################################

def get_seats_th2_a():
 import tkinter as tk
 root = tk.Tk()
 root.geometry("525x350")
 root.configure(bg = "gray")
 root.resizable(False,False)
 root.title("Seat credentials")

 frame = Frame(root,width=1200,height=1500,bg='gray')
 frame.place(x=0,y=0)

 def on_enter(e):
    seat.delete(0,'end')
 def on_leave(e):
    name=seat.get()
    if name=='':
        seat.insert(0,'How many seats do you want to book.?')
 seat = Entry(frame,width = 40, fg="black",bg = "white", border = 4,font = ("Times new roman",11,"bold"))
 seat.place(x = 50,y = 14)
 seat.insert(0,"How many seats do you want to book.?")
 seat.bind('<FocusIn>',on_enter)
 seat.bind('<FocusOut>',on_leave)

 def entry_th2_a():
    enter_text = seat.get()
    try:
        num_seats = int(enter_text)
        if num_seats > 0:
            book_seats_th2_a()
        else:
            messagebox.showerror("Invalid", "Enter a valid input")
    except ValueError:
        messagebox.showerror("Invalid", "Enter a valid input")

 Button(frame, height=0, width=15, pady=4, text='Enter ↓', bg='red', command=entry_th2_a,font=('Times New Roman', 10, 'bold'), fg='white', border=2.0).place(x=150, y=93)

 def show_selected_time():
   global selected_time
   selected_time = time_var.get()
   selected_time
   
 time_var = tk.StringVar(root)
 time_var.set("Select a show time")

 time_option_menu = tk.OptionMenu(root, time_var, "10:00 AM", "2:00 PM", "6:00 PM", "9:00 PM", "11:00 PM")
 time_option_menu.place(x=110,y=45)
 
 show_button = tk.Button(root, text="OK", command=show_selected_time)
 show_button.place(x=260,y=50)

 root.mainloop() 

######################################################################################



def display_booking_details_th2_a(movie_name, num_seats, show_time, theater):
    messagebox.showinfo("Ticket Booked", f"Movie: {movie_name}\nNumber of Seats: {num_seats}\nShow Time: {show_time}\nTheater: {theater}")



def book_seats_th2_a():
    root = tk.Tk()
    root.title("Movie Seat Selection")

    canvas = tk.Canvas(root, width=1000, height=500)
    canvas.pack()

    seats = []
    for row in range(12):
        for col in range(13):
            seat = canvas.create_rectangle(col*40, row*40, col*40+30, row*40+30, fill="green")
            seats.append(seat)

    # Add movie screen
    screen = canvas.create_rectangle(00, 480, 530, 600, fill="black")

    def toggle_seat_th2_a(seat):
        if canvas.itemcget(seat, "fill") == "green":
            canvas.itemconfig(seat, fill="red")
        else:
            canvas.itemconfig(seat, fill="green")
            
            
    def confirm_booking_th2_a():
        selected_seats = []
        for seat in seats:
            if canvas.itemcget(seat, "fill") == "red":
                selected_seats.append(seat)

        if len(selected_seats) > 0:
            num_seats = len(selected_seats)
            movie_name = "Horrors of the heart"  # Replace with the actual movie name
            show_time = f"{selected_time}"  # Replace with the actual show time
            theater = "Inox theatre"  # Replace with the actual theater name

            display_booking_details_th2_a(movie_name, num_seats, show_time, theater)
        else:
            messagebox.showerror("Error", "No seats selected!")

    for seat in seats:
        button = tk.Button(root, text="", command=lambda s=seat: toggle_seat_th2_a(s))
        button.place(x=canvas.coords(seat)[0]+5, y=canvas.coords(seat)[1]+5)

    screen_label = Label(root, text=" <<<<<<<<  This side screen  >>>>>>>> ",fg = "white",bg = "black",font = ("times new roman",12,"bold"))
    canvas.create_window(285, 490, window = screen_label)
       
      
    confirm_button = tk.Button(root, text="Confirm Booking",bg = "red",fg="white", command=confirm_booking_th2_a)
    confirm_button.pack()

    root.mainloop()
    #root.destroy()
    
#############################################################################################################################

################################## SEAT BOOKING FOR TH2 M2 ##############################################

def get_seats_th2_b():
 import tkinter as tk
 root = tk.Tk()
 root.geometry("525x350")
 root.configure(bg = "gray")
 root.resizable(False,False)
 root.title("Seat credentials")

 frame = Frame(root,width=1200,height=1500,bg='gray')
 frame.place(x=0,y=0)

 def on_enter(e):
    seat.delete(0,'end')
 def on_leave(e):
    name=seat.get()
    if name=='':
        seat.insert(0,'How many seats do you want to book.?')
 seat = Entry(frame,width = 40, fg="black",bg = "white", border = 4,font = ("Times new roman",11,"bold"))
 seat.place(x = 50,y = 14)
 seat.insert(0,"How many seats do you want to book.?")
 seat.bind('<FocusIn>',on_enter)
 seat.bind('<FocusOut>',on_leave)

 def entry_th2_b():
    enter_text = seat.get()
    try:
        num_seats = int(enter_text)
        if num_seats > 0:
            book_seats_th2_b()
        else:
            messagebox.showerror("Invalid", "Enter a valid input")
    except ValueError:
        messagebox.showerror("Invalid", "Enter a valid input")

 Button(frame, height=0, width=15, pady=4, text='Enter ↓', bg='red', command=entry_th2_b,font=('Times New Roman', 10, 'bold'), fg='white', border=2.0).place(x=150, y=93)

 def show_selected_time():
   global selected_time
   selected_time = time_var.get()
   selected_time
   
 time_var = tk.StringVar(root)
 time_var.set("Select a show time")

 time_option_menu = tk.OptionMenu(root, time_var, "10:00 AM", "2:00 PM", "6:00 PM", "9:00 PM", "11:00 PM")
 time_option_menu.place(x=110,y=45)
 
 show_button = tk.Button(root, text="OK", command=show_selected_time)
 show_button.place(x=260,y=50)

 root.mainloop() 

######################################################################################



def display_booking_details_th2_b(movie_name, num_seats, show_time, theater):
    messagebox.showinfo("Ticket Booked", f"Movie: {movie_name}\nNumber of Seats: {num_seats}\nShow Time: {show_time}\nTheater: {theater}")



def book_seats_th2_b():
    root = tk.Tk()
    root.title("Movie Seat Selection")

    canvas = tk.Canvas(root, width=1000, height=500)
    canvas.pack()

    seats = []
    for row in range(12):
        for col in range(13):
            seat = canvas.create_rectangle(col*40, row*40, col*40+30, row*40+30, fill="green")
            seats.append(seat)

    # Add movie screen
    screen = canvas.create_rectangle(00, 480, 530, 600, fill="black")

    def toggle_seat_th2_b(seat):
        if canvas.itemcget(seat, "fill") == "green":
            canvas.itemconfig(seat, fill="red")
        else:
            canvas.itemconfig(seat, fill="green")
            
            
    def confirm_booking_th2_b():
        selected_seats = []
        for seat in seats:
            if canvas.itemcget(seat, "fill") == "red":
                selected_seats.append(seat)

        if len(selected_seats) > 0:
            num_seats = len(selected_seats)
            movie_name = "Por thozhil"  # Replace with the actual movie name
            show_time = f"{selected_time}"  # Replace with the actual show time
            theater = "Inox theatre"  # Replace with the actual theater name

            display_booking_details_th2_b(movie_name, num_seats, show_time, theater)
        else:
            messagebox.showerror("Error", "No seats selected!")

    for seat in seats:
        button = tk.Button(root, text="", command=lambda s=seat: toggle_seat_th2_b(s))
        button.place(x=canvas.coords(seat)[0]+5, y=canvas.coords(seat)[1]+5)

    screen_label = Label(root, text=" <<<<<<<<  This side screen  >>>>>>>> ",fg = "white",bg = "black",font = ("times new roman",12,"bold"))
    canvas.create_window(285, 490, window = screen_label)
       
      
    confirm_button = tk.Button(root, text="Confirm Booking",bg = "red",fg="white", command=confirm_booking_th2_b)
    confirm_button.pack()

    root.mainloop()
    #root.destroy()
    
#############################################################################################################################
################################## SEAT BOOKING FOR TH3 M1 ##############################################

def get_seats_th3_a():
 import tkinter as tk
 root = tk.Tk()
 root.geometry("525x350")
 root.configure(bg = "gray")
 root.resizable(False,False)
 root.title("Seat credentials")

 frame = Frame(root,width=1200,height=1500,bg='gray')
 frame.place(x=0,y=0)

 def on_enter(e):
    seat.delete(0,'end')
 def on_leave(e):
    name=seat.get()
    if name=='':
        seat.insert(0,'How many seats do you want to book.?')
 seat = Entry(frame,width = 40, fg="black",bg = "white", border = 4,font = ("Times new roman",11,"bold"))
 seat.place(x = 50,y = 14)
 seat.insert(0,"How many seats do you want to book.?")
 seat.bind('<FocusIn>',on_enter)
 seat.bind('<FocusOut>',on_leave)

 def entry_th3_a():
    enter_text = seat.get()
    try:
        num_seats = int(enter_text)
        if num_seats > 0:
            book_seats_th3_a()
        else:
            messagebox.showerror("Invalid", "Enter a valid input")
    except ValueError:
        messagebox.showerror("Invalid", "Enter a valid input")

 Button(frame, height=0, width=15, pady=4, text='Enter ↓', bg='red', command=entry_th3_a,font=('Times New Roman', 10, 'bold'), fg='white', border=2.0).place(x=150, y=93)

 def show_selected_time():
   global selected_time
   selected_time = time_var.get()
   selected_time
   
 time_var = tk.StringVar(root)
 time_var.set("Select a show time")

 time_option_menu = tk.OptionMenu(root, time_var, "10:00 AM", "2:00 PM", "6:00 PM", "9:00 PM", "11:00 PM")
 time_option_menu.place(x=110,y=45)
 
 show_button = tk.Button(root, text="OK", command=show_selected_time)
 show_button.place(x=260,y=50)

 root.mainloop() 

######################################################################################



def display_booking_details_th3_a(movie_name, num_seats, show_time, theater):
    messagebox.showinfo("Ticket Booked", f"Movie: {movie_name}\nNumber of Seats: {num_seats}\nShow Time: {show_time}\nTheater: {theater}")



def book_seats_th3_a():
    root = tk.Tk()
    root.title("Movie Seat Selection")

    canvas = tk.Canvas(root, width=1000, height=500)
    canvas.pack()

    seats = []
    for row in range(12):
        for col in range(13):
            seat = canvas.create_rectangle(col*40, row*40, col*40+30, row*40+30, fill="green")
            seats.append(seat)

    # Add movie screen
    screen = canvas.create_rectangle(00, 480, 530, 600, fill="black")

    def toggle_seat_th3_a(seat):
        if canvas.itemcget(seat, "fill") == "green":
            canvas.itemconfig(seat, fill="red")
        else:
            canvas.itemconfig(seat, fill="green")
            
            
    def confirm_booking_th3_a():
        selected_seats = []
        for seat in seats:
            if canvas.itemcget(seat, "fill") == "red":
                selected_seats.append(seat)

        if len(selected_seats) > 0:
            num_seats = len(selected_seats)
            movie_name = "Asvins"  # Replace with the actual movie name
            show_time = f"{selected_time}"  # Replace with the actual show time
            theater = "Sk_Miraj theatre"  # Replace with the actual theater name

            display_booking_details_th3_a(movie_name, num_seats, show_time, theater)
        else:
            messagebox.showerror("Error", "No seats selected!")

    for seat in seats:
        button = tk.Button(root, text="", command=lambda s=seat: toggle_seat_th3_a(s))
        button.place(x=canvas.coords(seat)[0]+5, y=canvas.coords(seat)[1]+5)

    screen_label = Label(root, text=" <<<<<<<<  This side screen  >>>>>>>> ",fg = "white",bg = "black",font = ("times new roman",12,"bold"))
    canvas.create_window(285, 490, window = screen_label)
       
      
    confirm_button = tk.Button(root, text="Confirm Booking",bg = "red",fg="white", command=confirm_booking_th3_a)
    confirm_button.pack()

    root.mainloop()
    #root.destroy()
    
#############################################################################################################################

################################## SEAT BOOKING FOR TH3 M2 ##############################################

def get_seats_th3_b():
 import tkinter as tk
 root = tk.Tk()
 root.geometry("525x350")
 root.configure(bg = "gray")
 root.resizable(False,False)
 root.title("Seat credentials")

 frame = Frame(root,width=1200,height=1500,bg='gray')
 frame.place(x=0,y=0)

 def on_enter(e):
    seat.delete(0,'end')
 def on_leave(e):
    name=seat.get()
    if name=='':
        seat.insert(0,'How many seats do you want to book.?')
 seat = Entry(frame,width = 40, fg="black",bg = "white", border = 4,font = ("Times new roman",11,"bold"))
 seat.place(x = 50,y = 14)
 seat.insert(0,"How many seats do you want to book.?")
 seat.bind('<FocusIn>',on_enter)
 seat.bind('<FocusOut>',on_leave)

 def entry_th3_b():
    enter_text = seat.get()
    try:
        num_seats = int(enter_text)
        if num_seats > 0:
            book_seats_th3_b()
        else:
            messagebox.showerror("Invalid", "Enter a valid input")
    except ValueError:
        messagebox.showerror("Invalid", "Enter a valid input")

 Button(frame, height=0, width=15, pady=4, text='Enter ↓', bg='red', command=entry_th3_b,font=('Times New Roman', 10, 'bold'), fg='white', border=2.0).place(x=150, y=93)

 def show_selected_time():
   global selected_time
   selected_time = time_var.get()
   selected_time
   
 time_var = tk.StringVar(root)
 time_var.set("Select a show time")

 time_option_menu = tk.OptionMenu(root, time_var, "10:00 AM", "2:00 PM", "6:00 PM", "9:00 PM", "11:00 PM")
 time_option_menu.place(x=110,y=45)
 
 show_button = tk.Button(root, text="OK", command=show_selected_time)
 show_button.place(x=260,y=50)

 root.mainloop() 

######################################################################################



def display_booking_details_th3_b(movie_name, num_seats, show_time, theater):
    messagebox.showinfo("Ticket Booked", f"Movie: {movie_name}\nNumber of Seats: {num_seats}\nShow Time: {show_time}\nTheater: {theater}")



def book_seats_th3_b():
    root = tk.Tk()
    root.title("Movie Seat Selection")

    canvas = tk.Canvas(root, width=1000, height=500)
    canvas.pack()

    seats = []
    for row in range(12):
        for col in range(13):
            seat = canvas.create_rectangle(col*40, row*40, col*40+30, row*40+30, fill="green")
            seats.append(seat)

    # Add movie screen
    screen = canvas.create_rectangle(00, 480, 530, 600, fill="black")

    def toggle_seat_th3_b(seat):
        if canvas.itemcget(seat, "fill") == "green":
            canvas.itemconfig(seat, fill="red")
        else:
            canvas.itemconfig(seat, fill="green")
            
            
    def confirm_booking_th3_b():
        selected_seats = []
        for seat in seats:
            if canvas.itemcget(seat, "fill") == "red":
                selected_seats.append(seat)

        if len(selected_seats) > 0:
            num_seats = len(selected_seats)
            movie_name = "The Thalainagaram-2"  # Replace with the actual movie name
            show_time = f"{selected_time}"  # Replace with the actual show time
            theater = "Sk_Miraj theatre"  # Replace with the actual theater name

            display_booking_details_th3_b(movie_name, num_seats, show_time, theater)
        else:
            messagebox.showerror("Error", "No seats selected!")

    for seat in seats:
        button = tk.Button(root, text="", command=lambda s=seat: toggle_seat_th3_b(s))
        button.place(x=canvas.coords(seat)[0]+5, y=canvas.coords(seat)[1]+5)

    screen_label = Label(root, text=" <<<<<<<<  This side screen  >>>>>>>> ",fg = "white",bg = "black",font = ("times new roman",12,"bold"))
    canvas.create_window(285, 490, window = screen_label)
       
      
    confirm_button = tk.Button(root, text="Confirm Booking",bg = "red",fg="white", command=confirm_booking_th3_b)
    confirm_button.pack()

    root.mainloop()
    #root.destroy()
    
#############################################################################################################################


            
############################################################################################################################


def Cinepolis_films():
    messagebox.showinfo("Information", "Selected Cinepolis theatres")
    root.destroy()
    Cinepolis_films1()

def Cinepolis_films1():
    win = Tk()
    win.geometry('925x500+700+200')
    win.title("Cinepolis")
    frame = Frame(win, width=3200, height=3500, bg='gray')
    frame.place(x=0, y=0)

    s_films=[]
    sm1 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Transformers-Rise of the beasts",command = get_seats_th1_a,font = ("Times new roman",11,"bold")).place(x = 50,y = 50)
    s_films.append(sm1)
    sm2 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Por thozhil",command = get_seats_th1_b,font = ("Times new roman",11,"bold")).place(x = 50,y = 90)
    s_films.append(sm2)

def Inox_films():
    messagebox.showinfo("Information", "Selected Inox theatres")
    root.destroy()
    Inox_films1()

def Inox_films1():
    win = Tk()
    win.geometry('925x500+700+200')
    win.title("Inox")
    frame = Frame(win, width=3200, height=3500, bg='gray')
    frame.place(x=0, y=0)
      
    st_films=[]
    st1 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Horrors of the heart",command = get_seats_th2_a,font = ("Times new roman",11,"bold")).place(x = 50,y = 50)
    st_films.append(st1)
    st2 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Por thozhil",command = get_seats_th2_b,font = ("Times new roman",11,"bold")).place(x = 50,y = 90)
    st_films.append(st2)


def Sk_Miraj_films():
    messagebox.showinfo("Information", "Selected Sk_Miraj theatres")
    root.destroy()
    Sk_Miraj_films1()

def Sk_Miraj_films1():
    win = Tk()
    win.geometry('925x500+700+200')
    win.title("Sk_Miraj")
    frame = Frame(win, width=3200, height=3500, bg='gray')
    frame.place(x=0, y=0)

    jt_films=[]
    jt1 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Asvins",command = get_seats_th3_a,font = ("Times new roman",11,"bold")).place(x = 50,y = 50)
    jt_films.append(jt1)
    jt2 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Thalainagaram-2",command = get_seats_th3_b,font = ("Times new roman",11,"bold")).place(x = 50,y = 90)
    jt_films.append(jt2)


def Coimbatore_theatres():


    at1 = Label(frame, width=68, fg="black", bg="sky blue", border=4, text="<<<< Theatres available in Coimbatore..! >>>>",
                font=("Times new roman", 11, "bold"))
    at1.place(x=5, y=12)


    l1 = Label(frame,width = 5, fg="white",bg = "black", border = 2,text="> T1",font = ("Times new roman",11,"bold"))
    l1.place(x = 50,y = 75)
    l2 = Label(frame,width = 5, fg="white",bg = "black", border = 2,text="> T2",font = ("Times new roman",11,"bold"))
    l2.place(x = 50,y = 115)
    l3 = Label(frame,width = 5, fg="white",bg = "black", border = 2,text="> T3",font = ("Times new roman",11,"bold"))
    l3.place(x = 50,y = 155)

    theatres = []
    t1=Button(frame,height=0,width = 65,pady=2,text='Cinepolis theatre',bg='red',command=Cinepolis_films,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=100,y=75)
    theatres.append(t1)
    t2=Button(frame,height=0,width = 65,pady=2,text='Inox max',bg='red',command = Inox_films,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=100,y=115)
    theatres.append(t2)
    t3=Button(frame,height=0,width = 65,pady=2,text='Sk_Miraj theatre',bg='red',command = Sk_Miraj_films,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=100,y=155)
    theatres.append(t3)



img= ImageTk.PhotoImage(file="C:/Users/adity/Documents/Python project 2023/Attachments/Select theatre.png",height=308,width=920)
Label(frame,image=img,bg="black").place(x = 0, y = 188)



Coimbatore_theatres()

root.mainloop()
