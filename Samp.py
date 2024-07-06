import tkinter as tk
from PIL import ImageTk, Image

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
    screen = canvas.create_rectangle(0, 480, 530, 600, fill="black")

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
            movie_name = "Por thozhil"  # Replace with the actual movie name
            show_time = f"{selected_time}"  # Replace with the actual show time
            theater = "Raja theatre"  # Replace with the actual theater name

            display_booking_details_th1_a(movie_name, num_seats, show_time, theater)
        else:
            messagebox.showerror("Error", "No seats selected!")

    for seat in seats:
        button = tk.Button(root, text="", command=lambda s=seat: toggle_seat_th1_a(s))
        button.place(x=canvas.coords(seat)[0]+5, y=canvas.coords(seat)[1]+5)
      
    # Add image
    image = ImageTk.PhotoImage(Image.open(r"D:\python program\Por thozhil r.png"))
    image_label = tk.Label(root, image=image,bg="black").place(x=560,y=5)
   # image_label.pack(anchor='e')
    #image_label.pack(anchor='ne')
    #image_label.pack(anchor='n')
    #image_label.pack(anchor='n')
    #image_label.pack()

    screen_label = tk.Label(root, text=" <<<<<<<<  This side screen  >>>>>>>> ", fg="white", bg="black", font=("times new roman", 12, "bold"))
    canvas.create_window(285, 490, window=screen_label)

    confirm_button = tk.Button(root, text="Confirm Booking", bg="red",command= confirm_booking_th1_a, fg="white")
    confirm_button.pack()

    root.mainloop()
    # root.destroy()

book_seats_th1_a()
