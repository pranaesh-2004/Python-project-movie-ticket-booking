import tkinter as tk
from moviepy.editor import VideoFileClip
from PIL import Image, ImageTk

def on_closing():
    splash_root.destroy()

def play_video():
    # Load the video
    video_path = r"D:\python program\Select movie video.mp4"
    clip = VideoFileClip(video_path)

    def update_frame(frame):
        frame_image = ImageTk.PhotoImage(image=Image.fromarray(frame))
        lbl.configure(image=frame_image)
        lbl.image = frame_image
        splash_root.update_idletasks()
        splash_root.update()

    for frame in clip.iter_frames(fps=24, with_times=False):
        update_frame(frame)

    # Destroy the root window after the video ends
    splash_root.destroy()

splash_root = tk.Tk()
splash_root.title("Welcome")
splash_root.geometry("925x500+700+200")
splash_root.configure(bg="white")
splash_root.resizable(False, False)

# Label to show while the video is loading
lbl = tk.Label(splash_root, bg="white")
lbl.pack(expand=True, fill="both")

splash_root.after(100, play_video)
splash_root.protocol("WM_DELETE_WINDOW", on_closing)
splash_root.mainloop()

import search
