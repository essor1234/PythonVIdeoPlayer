import tkinter as tk
import tkinter.ttk as ttk

from UI.video_manager import VideoManager
from UI.playlist_manager import PlaylistManager
class MainWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.show_video_player_frame()

    def show_frame(self, frame_classname):
        frame = frame_classname(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def show_video_player_frame(self):
        self.show_frame(VideoPlayer)


class VideoPlayer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # frame button
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(column=0, row=0)

        # video manager button
        self.video_manager_btn = ttk.Button(self.main_frame, text="Video Manager", command= self.open_video_manager)
        self.video_manager_btn.config(width=40)
        self.video_manager_btn.grid(row=0, column=0, padx=5, pady=5)

        # playlist manager button
        self.playlist_manager_btn = ttk.Button(self.main_frame, text="Playlist Manager", command= self.open_list_manager)
        self.playlist_manager_btn.config(width=40)
        self.playlist_manager_btn.grid(row=1, column=0, padx=5, pady=5)

    def open_video_manager(self):
        new_window = tk.Toplevel(self.master)
        # create a CheckVideo frame inside the new window
        check_video_frame = VideoManager(new_window)
        # create name
        new_window.title("Check Video")
        # pack the CheckVideo frame
        check_video_frame.pack()

    def open_list_manager(self):
        new_window = tk.Toplevel(self.master)
        # create a CheckVideo frame inside the new window
        check_video_frame = PlaylistManager(new_window)
        # create name
        new_window.title("Check Video")
        # pack the CheckVideo frame
        check_video_frame.pack()

# root = tk.Tk()
# root.title("Video Player")
#
# # create an instance of VideoPlayer and pass root as the parent and the controller
# video_player = VideoPlayer(root, root)
# video_player.pack(fill="both", expand=True)
#
# # start the main loop
# root.mainloop()