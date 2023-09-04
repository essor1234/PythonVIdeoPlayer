import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

class AddVideo(tk.Frame):
    def __init__(self, parent, video_manager):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.update_video = video_manager
        # Use for display warning
        self.warning_shown = False

        # window display
        self.root = self.parent
        self.root.title("Add Video")

        """Button"""
        # from my computer
        self.my_computer_btn = ttk.Button(self.root, text="From My Computer", width=50)
        self.my_computer_btn.grid(row=0, column=0, padx=10, pady=10)
        # from Youtube
        self.yt_btn = ttk.Button(self.root, text="From Youtube", width=50)
        self.yt_btn.grid(row=1, column=0, padx=10, pady=10)

if __name__ == "__main__":
    # Create a themed window with the desired theme name
    window = ThemedTk(theme="arc")
    # Create a style object
    style = ttk.Style(window)


    app = AddVideo(window, None)
    window.mainloop()

