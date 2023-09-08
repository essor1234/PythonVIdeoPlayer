import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

from UI.my_comp import FromMyComputer
from UI.from_youtube import FromYoutube

class AddVideo(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        # Use for display warning
        self.warning_shown = False
        # use for window display
        self.top_open = False
        # window display
        self.root = self.parent
        self.root.title("Add Video")

        """Button"""
        # from my computer
        self.my_computer_btn = ttk.Button(self.root, text="From My Computer", width=50,
                                          command=self.my_computer_video)
        self.my_computer_btn.grid(row=0, column=0, padx=10, pady=10)
        # from Youtube
        self.yt_btn = ttk.Button(self.root, text="From Youtube", width=50,
                                 command=self.youtube_video)
        self.yt_btn.grid(row=1, column=0, padx=10, pady=10)

    def my_computer_video(self):
        if not self.top_open:
            self.top_open = True
            new_window = tk.Toplevel(self)
            # create a CheckVideo frame inside the new window
            check_video_frame = FromMyComputer(new_window, self)
            # create name
            check_video_frame.grid()
            new_window.protocol("WM_DELETE_WINDOW", lambda: self.close_top(new_window))

    def youtube_video(self):
        if not self.top_open:
            self.top_open = True
            new_window = tk.Toplevel(self)
            # create a CheckVideo frame inside the new window
            check_video_frame = FromYoutube(new_window, self)
            # create name
            check_video_frame.grid()
            new_window.protocol("WM_DELETE_WINDOW", lambda: self.close_top(new_window))
    # use for prevent multiple instances
    def close_top(self, top_window):
        self.top_open = False
        # Destroy the Toplevel window
        top_window.destroy()

if __name__ == "__main__":
    # Create a themed window with the desired theme name
    window = ThemedTk(theme="arc")
    # Create a style object
    style = ttk.Style(window)

    app = AddVideo(window)
    window.mainloop()

