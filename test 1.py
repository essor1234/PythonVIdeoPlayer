import tkinter as tk
from tkinter import ttk
import cv2
import threading

from PIL import ImageTk


class VideoPlayer(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.video_file = "data/videos_stored/glimpse of us.mp4"

        self.cv_img = cv2.cvtColor(cv2.imread('a horse.jpg'), cv2.COLOR_BGR2RGB)
        self.height, self.width, _ = self.cv_img.shape
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack()
        self.current_frame = cv2.imread(self.video_file, 0)
        self.canvas.create_image(0, 0, image=self.current_frame, anchor=tk.NW)

        self.btn_play = tk.Button(self, text="Play", command=NotImplemented)

        self.progressbar = ttk.Progressbar(self, length=500)

        self.vol_scale = ttk.Scale(self, from_=0, to=1, command=NotImplemented)

        self.btn_full_screen = tk.Button(self, text="Full Screen", command=NotImplemented)

        self.btn_forward = tk.Button(self, text="Forward", command=NotImplemented)
        self.btn_back = tk.Button(self, text="Back", command=NotImplemented)

        self.pack()

        self.video_paused = True
        self.video_position = 0.0
    #
    # def show_frame(self):
    #     ret, frame = self.capture.read()
    #
    #     if ret:
    #         print("Frame shape:", frame.shape)
    #     else:
    #         print("Error reading frame")
    #
    #     if ret:
    #         self.photo = ImageTk.PhotoImage(image=tk.Image.fromarray(frame))
    #         self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
    #
    # def play_video(self):
    #     self.video_paused = False
    #     threading.Thread(target=self.play_threaded, daemon=True).start()
    #
    # def play_threaded(self):
    #     # Logic to play video
    #     pass
    #
    # # Other functions
    # def full_screen(self):
    #     pass
    #
    # def set_volume(self, value):
    #     pass
    #
    # def forward(self):
    #     pass
    #
    # def back(self):
    #     pass

root = tk.Tk()
video_player = VideoPlayer(root)
root.mainloop()
