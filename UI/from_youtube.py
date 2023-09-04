import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk


class FromYoutube(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent
        self.parent.title("From Youtube")

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
        self.get_rate_lbl = ttk.Label(self.parent, text="URL: ")
        self.get_rate_lbl.grid(row=3, column=0, padx=5, pady=5)
        # path entry
        self.get_rate = tk.Entry(self.parent, highlightthickness=1)
        self.get_rate.grid(row=3, column=1, columnspan=3, sticky="w", padx=5, pady=5)

        # save button
        self.save_btn = ttk.Button(self.parent, text="Save", command=None)
        self.save_btn.config(width=50)
        self.save_btn.grid(columnspan=3, padx=5, pady=5)


if __name__ == "__main__":
    # Create a themed window with the desired theme name
    window = ThemedTk(theme="arc")
    # Create a style object
    style = ttk.Style(window)

    app = FromYoutube(window, None)
    window.mainloop()