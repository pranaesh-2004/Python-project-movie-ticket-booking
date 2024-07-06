import tkinter as tk
from tkinter import Frame, Entry, Button, messagebox, Label, Canvas, Toplevel
from PIL import ImageTk

# Global variables
import tkinter as tk
from tkinter import Frame, Entry, Button, messagebox, Label, Canvas, Toplevel
from PIL import ImageTk

# Global variables
seat_status = [['green' for _ in range(13)] for _ in range(10)]  # Reduced to 10 rows
num_seats_to_book = 0
selected_time = ""

def display_booking_details_th1_a(movie_name, num_seats, show_time, theater, total_price, selected_seats):
    ticket_details = f"""
    ----------------------------------
    Movie Ticket
    ----------------------------------
    Movie: {movie_name}
    Theater: {theater}
    Show Time: {show_time}
    Number of Seats: {num_seats}
    Seats: {', '.join(selected_seats)}
    Total Price: Rs. {total_price}
    ----------------------------------
    Enjoy the show!
    """
    messagebox.showinfo("Ticket Booked", ticket_details)

def book_seats_th1_a():
    global num_seats_to_book
    root = Toplevel()
    root.title("Movie Seat Selection")

    canvas = Canvas(root, width=1000, height=500)  # Adjusted height to 500 for fewer rows
    canvas.pack()

    seats = []
    row_labels = "ABCDEFGHIJ"  # Adjusted for fewer rows

    # Add movie screen
    screen = canvas.create_rectangle(0, 0, 530, 50, fill="black")
    screen_label = Label(root, text=" <<<<<<<<  Screen  >>>>>>>> ", fg="white", bg="black",
                         font=("times new roman", 12, "bold"))
    canvas.create_window(265, 25, window=screen_label)

    # Create regular rows
    for row in range(10):
        for col in range(13):
            color = seat_status[row][col]
            seat_label = f"{row_labels[row]}{col+1}"
            seat = canvas.create_rectangle(col * 40, row * 40 + 50, col * 40 + 30, row * 40 + 80, fill=color)
            seats.append((row, col, seat, seat_label))
            canvas.create_text(col * 40 + 15, row * 40 + 65, text=seat_label, fill="black")

    # Load and display the image on the canvas
    image_path = "Select theatre.png"  # Replace with the actual path to your image
    try:
        image = ImageTk.PhotoImage(file=image_path)
        image_label = canvas.create_image(600, 0, anchor="nw", image=image)
    except FileNotFoundError:
        messagebox.showerror("Image Error", "Image file not found. Please check the path.")

    selected_seats_count = 0

    def toggle_seat_th1_a(seat):
        nonlocal selected_seats_count
        row, col, seat_id, seat_label = seat
        if canvas.itemcget(seat_id, "fill") == "green":
            if selected_seats_count < num_seats_to_book:
                canvas.itemconfig(seat_id, fill="red")
                selected_seats_count += 1
            else:
                messagebox.showerror("Error", f"You can only select {num_seats_to_book} seats.")
        elif canvas.itemcget(seat_id, "fill") == "red":
            canvas.itemconfig(seat_id, fill="green")
            selected_seats_count -= 1

    def confirm_booking_th1_a():
        selected_seats = []
        for row, col, seat_id, seat_label in seats:
            if canvas.itemcget(seat_id, "fill") == "red":
                selected_seats.append(seat_label)
                seat_status[row][col] = "red"

        if len(selected_seats) == num_seats_to_book:
            num_seats = len(selected_seats)
            movie_name = "Por thozhil"  # Replace with the actual movie name
            show_time = selected_time  # Use the actual selected show time
            theater = "Raja theatre"  # Replace with the actual theater name

            ticket_rate = 120
            total_price = num_seats * ticket_rate

            display_booking_details_th1_a(movie_name, num_seats, show_time, theater, total_price, selected_seats)
            root.destroy()
        else:
            messagebox.showerror("Error", f"Please select exactly {num_seats_to_book} seats.")

    for row, col, seat_id, seat_label in seats:
        button = tk.Button(root, text="", command=lambda s=(row, col, seat_id, seat_label): toggle_seat_th1_a(s))
        button.place(x=canvas.coords(seat_id)[0] + 5, y=canvas.coords(seat_id)[1] + 5)

    confirm_button = tk.Button(root, text="Confirm Booking", bg="red", fg="white", command=confirm_booking_th1_a)
    confirm_button.pack()

    root.mainloop()

def get_seats_th1_a():
    global num_seats_to_book

    root = tk.Tk()
    root.geometry("525x350")
    root.configure(bg="gray")
    root.resizable(False, False)
    root.title("Seat credentials")

    frame = Frame(root, width=1200, height=1500, bg='gray')
    frame.place(x=0, y=0)

    def on_enter(e):
        seat.delete(0, 'end')

    def on_leave(e):
        name = seat.get()
        if name == '':
            seat.insert(0, 'How many seats do you want to book.?')

    seat = Entry(frame, width=40, fg="black", bg="white", border=4, font=("Times new roman", 11, "bold"))
    seat.place(x=50, y=14)
    seat.insert(0, "How many seats do you want to book.?")
    seat.bind('<FocusIn>', on_enter)
    seat.bind('<FocusOut>', on_leave)

    def entry_th1_a():
        global num_seats_to_book
        enter_text = seat.get()
        try:
            num_seats_to_book = int(enter_text)
            if num_seats_to_book > 0:
                book_seats_th1_a()
            else:
                messagebox.showerror("Invalid", "Enter a valid input")
        except ValueError:
            messagebox.showerror("Invalid", "Enter a valid input")

    Button(frame, height=0, width=15, pady=4, text='Enter ↓', bg='red', command=entry_th1_a,
           font=('Times New Roman', 10, 'bold'), fg='white', border=2.0).place(x=150, y=93)

    def show_selected_time():
        global selected_time
        selected_time = time_var.get()

    time_var = tk.StringVar(root)
    time_var.set("Select a show time")

    time_option_menu = tk.OptionMenu(root, time_var, "10:00 AM", "2:00 PM", "6:00 PM", "9:00 PM", "11:00 PM")
    time_option_menu.place(x=110, y=45)

    show_button = tk.Button(root, text="OK", command=show_selected_time)
    show_button.place(x=260, y=50)

    root.mainloop()

# Call the function to start the program
get_seats_th1_a()


#root.mainloop()
    
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
    root = tk.Toplevel()
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

    image_path =r"D:\python program\Adipurush.jpg" 
    image = ImageTk.PhotoImage(file=image_path)
    image_label = canvas.create_image(540, 0, anchor="nw", image=image)


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
            movie_name = "Adipurush"  # Replace with the actual movie name
            show_time = f"{selected_time}"  # Replace with the actual show time
            theater = "Raja theatre"  # Replace with the actual theater name

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
            movie_name = "The Flash"  # Replace with the actual movie name
            show_time = f"{selected_time}"  # Replace with the actual show time
            theater = "Surya theatre"  # Replace with the actual theater name

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
            movie_name = "Regina"  # Replace with the actual movie name
            show_time = f"{selected_time}"  # Replace with the actual show time
            theater = "Surya theatre"  # Replace with the actual theater name

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
            movie_name = "Spiderman-across the spiderverse"  # Replace with the actual movie name
            show_time = f"{selected_time}"  # Replace with the actual show time
            theater = "Janagar theatre"  # Replace with the actual theater name

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
            movie_name = "The Elemental"  # Replace with the actual movie name
            show_time = f"{selected_time}"  # Replace with the actual show time
            theater = "Janagar theatre"  # Replace with the actual theater name

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


def raja_films():
    messagebox.showinfo("Information", "Selected Raja theatres")
    root.destroy()
    raja_films1()

def raja_films1():
    win = Tk()
    win.geometry('925x500+700+200')
    win.title("Raja")
    frame = Frame(win, width=3200, height=3500, bg='gray')
    frame.place(x=0, y=0)

    s_films=[]
    sm1 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Por thozhil",command = get_seats_th1_a,font = ("Times new roman",11,"bold")).place(x = 50,y = 50)
    s_films.append(sm1)
    sm2 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Adipurush",command = get_seats_th1_b,font = ("Times new roman",11,"bold")).place(x = 50,y = 90)
    s_films.append(sm2)
    
def surya_films():
    messagebox.showinfo("Information", "Selected Surya theatres")
    root.destroy()
    surya_films1()

def surya_films1():
    win = Tk()
    win.geometry('925x500+700+200')
    win.title("Surya")
    frame = Frame(win, width=3200, height=3500, bg='gray')
    frame.place(x=0, y=0)
      
    st_films=[]
    st1 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="The Flash",command = get_seats_th2_a,font = ("Times new roman",11,"bold")).place(x = 50,y = 50)
    st_films.append(st1)
    st2 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Regina",command = get_seats_th2_b,font = ("Times new roman",11,"bold")).place(x = 50,y = 90)
    st_films.append(st2)


def janagar_films():
    messagebox.showinfo("Information", "Selected Janagar theatres")
    root.destroy()
    janagar_films1()

def janagar_films1():
    win = Tk()
    win.geometry('925x500+700+200')
    win.title("Janagar")
    frame = Frame(win, width=3200, height=3500, bg='gray')
    frame.place(x=0, y=0)

    jt_films=[]
    jt1 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Spiderman-across the spiderverse",command = get_seats_th3_a,font = ("Times new roman",11,"bold")).place(x = 50,y = 50)
    jt_films.append(jt1)
    jt2 = Button(frame,height = 0,width= 65,pady=2,fg="black",bg = "sky blue", border = 0,text="Elemental",command = get_seats_th3_b,font = ("Times new roman",11,"bold")).place(x = 50,y = 90)
    jt_films.append(jt2)


def ariyalur_theatres():


    at1 = Label(frame, width=68, fg="black", bg="sky blue", border=4, text="<<<< Theatres available in Aliyalur..! >>>>",
                font=("Times new roman", 11, "bold"))
    at1.place(x=5, y=12)


    l1 = Label(frame,width = 5, fg="white",bg = "black", border = 2,text="> T1",font = ("Times new roman",11,"bold"))
    l1.place(x = 50,y = 75)
    l2 = Label(frame,width = 5, fg="white",bg = "black", border = 2,text="> T2",font = ("Times new roman",11,"bold"))
    l2.place(x = 50,y = 115)
    l3 = Label(frame,width = 5, fg="white",bg = "black", border = 2,text="> T3",font = ("Times new roman",11,"bold"))
    l3.place(x = 50,y = 155)

    theatres = []
    t1=Button(frame,height=0,width = 65,pady=2,text='Raja theatre',bg='red',command=raja_films,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=100,y=75)
    theatres.append(t1)
    t2=Button(frame,height=0,width = 65,pady=2,text='Surya max',bg='red',command = surya_films,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=100,y=115)
    theatres.append(t2)
    t3=Button(frame,height=0,width = 65,pady=2,text='Janagar theatre',bg='red',command = janagar_films,font=('Times New Roman',10,'bold'),fg='white',border=0).place(x=100,y=155)
    theatres.append(t3)



img= ImageTk.PhotoImage(file=r"D:\python program\Select theatre.png",height=308,width=920)
Label(frame,image=img,bg="black").place(x = 0, y = 188)



ariyalur_theatres()

root.mainloop()
