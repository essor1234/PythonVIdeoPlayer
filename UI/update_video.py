import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

class UpdateVideo(tk.Frame):
    def __init__(self, parent, video_manager):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.update_video = video_manager
        # Use for display warning
        self.warning_shown = False

        # window display
        self.root = self.parent
        self.root.title("Update")

        """Entry"""
        # Frame for entry
        self.get_frame = ttk.Frame(self.root)
        self.get_frame.grid(column=0, row=0)
        # Title label
        self.get_title_lbl = ttk.Label(self.get_frame, text="Title: ")
        self.get_title_lbl.grid(row=0, column=0, padx=5, pady=5)
        # title entry
        self.get_title = tk.Entry(self.get_frame, highlightthickness=1)
        self.get_title.grid(row=0, column=1, columnspan=3, sticky="w", padx=5, pady=5)

        # director label
        self.get_director_lbl = ttk.Label(self.get_frame, text="Director: ")
        self.get_director_lbl.grid(row=1, column=0, padx=5, pady=5)
        # director entry
        self.get_director = tk.Entry(self.get_frame, highlightthickness=1)
        self.get_director.grid(row=1, column=1, columnspan=3, sticky="w", padx=5, pady=5)

        # rate label
        self.get_rate_lbl = ttk.Label(self.get_frame, text="Rate: ")
        self.get_rate_lbl.grid(row=2, column=0, padx=5, pady=5)
        # rate entry
        self.get_rate = tk.Entry(self.get_frame, highlightthickness=1)
        self.get_rate.grid(row=2, column=1, columnspan=3, sticky="w", padx=5, pady=5)

        # path label
        self.get_rate_lbl = ttk.Label(self.get_frame, text="Path: ")
        self.get_rate_lbl.grid(row=3, column=0, padx=5, pady=5)
        # path entry
        self.get_rate = tk.Entry(self.get_frame, highlightthickness=1)
        self.get_rate.grid(row=3, column=1, columnspan=3, sticky="w", padx=5, pady=5)



        # plays label
        self.get_plays_lbl = ttk.Label(self.get_frame, text="Plays: ")
        self.get_plays_lbl.grid(row=4, column=0, padx=5, pady=5)
        # plays listbox
        self.get_plays = tk.Listbox(self.get_frame, height=1, width=10)
        self.get_plays.grid(row=4, column=1, columnspan=3, sticky="w", padx=5, pady=5)

        # plays reset button
        self.reset_btn = ttk.Button(self.get_frame, text="Reset", command=None)
        self.reset_btn.grid(row=4, column=2, columnspan=3, padx=5, pady=5)


        # save button
        self.save_btn = ttk.Button(self.root, text="Save", command=None)
        self.save_btn.config(width=50)
        self.save_btn.grid(columnspan=3, padx=5, pady=5)


if __name__ == "__main__":
    # Create a themed window with the desired theme name
    window = ThemedTk(theme="arc")
    # Create a style object
    style = ttk.Style(window)


    app = UpdateVideo(window, None)
    window.mainloop()