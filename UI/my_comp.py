import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

from models.VIdeo_model import Video

class FromMyComputer(tk.Frame, Video):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent
        self.parent.title("From My Computer")

        # Title label
        self.get_title_lbl = ttk.Label(self.parent, text="Title: ")
        self.get_title_lbl.grid(row=0, column=0, padx=5, pady=5)
        # title entry
        self.get_title = tk.Entry(self.parent, highlightthickness=1)
        self.get_title.grid(row=0, column=1, columnspan=3, sticky="w", padx=5, pady=5)

        # director label
        self.get_director_lbl = ttk.Label(self.parent, text="Director: ")
        self.get_director_lbl.grid(row=1, column=0, padx=5, pady=5)
        # director entry
        self.get_director = tk.Entry(self.parent, highlightthickness=1)
        self.get_director.grid(row=1, column=1, columnspan=3, sticky="w", padx=5, pady=5)

        # path label
        self.get_path_lbl = ttk.Label(self.parent, text="Path: ")
        self.get_path_lbl.grid(row=3, column=0, padx=5, pady=5)
        # path entry
        self.get_path = tk.Entry(self.parent, highlightthickness=1)
        self.get_path.grid(row=3, column=1, columnspan=3, sticky="w", padx=5, pady=5)
        # Choose video button
        self.video_btn = ttk.Button(self.parent, text="Choose Video",
                                    command= self.choose_video)
        self.video_btn.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        # save button
        self.save_btn = ttk.Button(self.parent, text="Save",
                                   command=self.save_video)
        self.save_btn.config(width=50)
        self.save_btn.grid(columnspan=3, padx=5, pady=5)

    def choose_video(self):

        self.filename, self.path = Video.choose_file(self)
        if self.path == False:
            pass
        self.get_path.delete(0, tk.END)
        self.get_path.insert(0, self.path)

    def save_video(self):
        current_title = self.get_title.get()
        current_director = self.get_director.get()
        current_path = self.get_path.get()
        """TODO: add waring later"""
        if not current_title:
            return False
        elif not current_director:
            return False
        elif not current_path:
            return False
        # run method
        Video.add_video_to_data(self, current_title, current_director, current_path)
        Video.move_file(self, self.filename, self.path)



if __name__ == "__main__":
    # Create a themed window with the desired theme name
    window = ThemedTk(theme="arc")
    # Create a style object
    style = ttk.Style(window)

    app = FromMyComputer(window, None)
    window.mainloop()