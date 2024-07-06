import tkinter as tk
from PIL import ImageTk, Image

movies = [("Por thozhil","C:\ADITYA.G\PYTHON FILES\Por.png")]

root = tk.Tk()
root.title("Movie List")

frame = tk.Frame(root)
frame.pack()

for movie, image_file in movies:
    image = Image.open(image_file)
    image = image.resize((150, 200))
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(frame, text=movie)
    label.pack(side=tk.LEFT, padx=10, pady=10)
    image_label = tk.Label(frame, image=photo)
    image_label.image = photo
    image_label.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()



