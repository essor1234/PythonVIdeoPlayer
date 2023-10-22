import tkinter as tk
import tkinter.ttk as ttk


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
        self.video_manager_btn = ttk.Button(self.main_frame, text="Video Manager", command=None)
        self.video_manager_btn.config(width=40)
        self.video_manager_btn.grid(row=0, column=0, padx=5, pady=5)

        # playlist manager button
        self.playlist_manager_btn = ttk.Button(self.main_frame, text="Playlist Manager", command=None)
        self.playlist_manager_btn.config(width=40)
        self.playlist_manager_btn.grid(row=1, column=0, padx=5, pady=5)


root = tk.Tk()
root.title("Video Player")

# create an instance of VideoPlayer and pass root as the parent and the controller
video_player = VideoPlayer(root, root)
video_player.pack(fill="both", expand=True)

# start the main loop
root.mainloop()