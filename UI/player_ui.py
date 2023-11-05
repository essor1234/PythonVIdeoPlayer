import tkinter as tk
import tkinter.ttk as ttk

from tkinter import *
from tkinter import filedialog

import datetime

import vlc

class PlayerUi(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.root = parent
        self.root.title("Player")

        self.load_btn = tk.Button(root, text="Load", command=self.load_video)
        self.load_btn.pack()

        self.vlc_player = vlc.MediaPlayer()

        self.play_pause_btn = tk.Button(root, text="Play", command=self.play_pause)
        self.play_pause_btn.pack()

        self.skip_plus_5sec = tk.Button(root, text="Skip -5 sec", command=lambda: self.skip(-5))
        self.skip_plus_5sec.pack(side="left")

        self.start_time = tk.Label(root, text=str(datetime.timedelta(seconds=0)))
        self.start_time.pack(side="left")

        self.progress_value = tk.IntVar(root)

        self.progress_slider = tk.Scale(root, variable=self.progress_value, from_=0, to=0, orient="horizontal", command=self.seek)
        # progress_slider.bind("<ButtonRelease-1>", seek)
        self.progress_slider.pack(side="left", fill="x", expand=True)

        self.end_time = tk.Label(root, text=str(datetime.timedelta(seconds=0)))
        self.end_time.pack(side="left")

        # Event bindings
        # Bind to time changed
        self.vlc_player.event_manager().event_attach(vlc.EventType.MediaPlayerTimeChanged,
                                                     self.update_scale)

        self.vlc_player.event_manager().event_attach(vlc.EventType.MediaPlayerESAdded,
                                                     self.video_ended)



        self.skip_plus_5sec = tk.Button(root, text="Skip +5 sec", command=lambda: self.skip(5))
        self.skip_plus_5sec.pack(side="left")

        self.vlc_player.video_set_decode_device("decoder")
        # Update slider every 100ms
        self.root.after(100, self.update_scale)

    # Call update_scale on time change
    def update_scale(self, event):
        self.progress_value.set(self.vlc_player.get_time() / 1000)


    def update_duration(self, event):
        """ updates the duration after finding the duration """
        duration = self.vlc_player.video_info()["duration"]
        self.end_time["text"] = str(datetime.timedelta(seconds=duration))
        self.progress_slider["to"] = duration

    def update_scale(self, event):
        """ updates the scale value """
        self.progress_value.set(self.vlc_player.current_duration())

    def load_video(self):

        file_path = filedialog.askopenfilename()

        media = vlc.Media(file_path)

        self.vlc_player.set_media(media)

    def seek(self, time):
        self.vlc_player.set_time(time * 1000)

    def skip(self, value: int):
        """ skip seconds """
        self.vlc_player.seek(int(self.progress_slider.get()) + value)
        self.progress_value.set(self.progress_slider.get() + value)

    def play_pause(self):
        if self.vlc_player.is_playing():
            self.vlc_player.pause()
        else:
            self.vlc_player.play()

    def video_ended(self, event):
        # VLC endTimeReached event handler
        self.vlc_player.stop()


root = tk.Tk()
app = PlayerUi(root)
app.mainloop()