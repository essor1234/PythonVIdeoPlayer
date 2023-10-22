import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
from ttkthemes import ThemedTk

class PlaylistManager(tk.Frame):
    columns = ["Id", "Title", "Length"]
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.parent= parent
        # window display
        self.root = self.parent
        self.root.title("Playlist Manager")

        """Search function"""
        # Create a frame for the search bar
        self.search_frame = ttk.Frame(self)
        self.search_frame.grid(row=0, column=3, columnspan=3, padx=5, pady=5, sticky="NE")

        # Create a label for the search bar
        search_label = ttk.Label(self.search_frame, text="Search by:")
        search_label.grid(row=0, column=0)

        # Create entry widget
        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.grid(row=0, column=1)

        # Create a list of search options
        search_options = ["Title", "Id"]
        # Create a variable to store the selected option
        self.selected_option = tk.StringVar()
        # Set the default value of the variable to the first option
        self.selected_option.set(search_options[0])
        # Create a Combobox for the search options
        self.search_combobox = ttk.Combobox(self.search_frame, textvariable=self.selected_option, values=search_options)
        self.search_combobox.config(width=10)
        self.search_combobox.grid(row=0, column=2)

        # Create a button to check a video
        btn_check_video = ttk.Button(self.search_frame, text="Search", compound="left",
                                     command=None)
        btn_check_video.config(width=15)
        btn_check_video.grid(row=0, column=3)
        # Create a frame for the buttons
        button_frame = ttk.Frame(self)
        button_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        """Warning area"""
        # Create a style object
        self.title_frame = ttk.Labelframe(self, borderwidth=0, relief="flat")
        self.title_frame.grid(row=0, column=1, padx=5, pady=5, sticky="N")
        my_font = tkfont.Font(family="Arial", size=20)
        # Create a label with the custom font and no border
        label = ttk.Label(self.title_frame, text="Welcome to Playlist Manager", font=my_font, borderwidth=0)
        label.grid(row=0, column=0, sticky="N")
        """Setting buttons"""
        self.function_btn_frame = ttk.Frame(self, relief="ridge", borderwidth=5)
        self.function_btn_frame.grid(row=0, column=0, padx=5, pady=5, sticky="W")
        # add button
        self.add_btn = ttk.Button(self.function_btn_frame, text="Create Playlist", compound="left",
                                  command=None)
        self.add_btn.grid(row=0, column=0, ipady=20, ipadx=20)
        # update button
        self.update_btn = ttk.Button(self.function_btn_frame, text="Update Playlist", compound="left",
                                  command=None)
        self.update_btn.grid(row=1, column=0, ipady=5, ipadx=5, padx=10, pady=10)
        # delete button
        self.delete_btn = ttk.Button(self.function_btn_frame, text="Delete Playlist", compound="left",
                                     command=None)
        self.delete_btn.grid(row=2, column=0, ipady=5, ipadx=5, padx=10, pady=10)

        """Display"""
        self.main_display = ttk.Treeview(self.title_frame, columns=self.columns, show="headings")
        self.main_display.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.main_display.column("Id", width=30, anchor="center")

        # Configure Treeview columns
        for col in self.columns:
            self.main_display.heading(col, text=col)


        self.listbox_frame = ttk.Frame(self)
        self.listbox_frame.grid(row=0, column=3, rowspan=2, padx=10, pady=10)
        # Create Listbox widget
        self.listbox = tk.Listbox(self.listbox_frame, height=12, width=60)
        self.listbox.grid(row=1, column=0, rowspan=2, padx=10, pady=10)

        """Play button"""
        self.play_btn = ttk.Button(self.listbox_frame, text="PLay", width=70)
        self.play_btn.grid(row=3, column=0, padx=10, pady=10)


if __name__ == "__main__":
    # Create a themed window with the desired theme name
    window = ThemedTk(theme="arc")
    # Create a style object
    style = ttk.Style(window)


    app = PlaylistManager(window, None)
    app.pack()
    window.mainloop()