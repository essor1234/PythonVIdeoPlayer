import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

class UpdatePlaylist(tk.Frame):
    columns_video = ["Id", "Title", "Director", "Rate"]

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.warning_shown = False
        # window display
        self.root = self.parent
        self.root.title("Update Playlist")

        """Search function"""
        self.search_frame = ttk.Frame(self.root)
        self.search_frame.pack(padx=10, pady=10, expand=True, anchor="center")

        # Create a label for the search bar
        self.search_label = ttk.Label(self.search_frame, text="Search by:")
        self.search_label.grid(row=0, column=0, padx=5, pady=5)

        # Create entry widget
        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a list of search options
        search_options = ["Title", "Director", "Rate", "Id"]
        # Create a variable to store the selected option
        self.selected_option = tk.StringVar()
        # Set the default value of the variable to the first option
        self.selected_option.set(search_options[0])
        # Create a Combobox for the search options
        self.search_combobox = ttk.Combobox(self.search_frame, textvariable=self.selected_option, values=search_options)
        self.search_combobox.config(width=10)
        self.search_combobox.grid(row=0, column=2, padx=5, pady=5)

        # Create a button to check a video
        btn_check_video = ttk.Button(self.search_frame, text="Search", compound="left",
                                     command=None)
        btn_check_video.config(width=15)
        btn_check_video.grid(row=0, column=3, padx=5, pady=5)


        # Create get name frame
        self.name_frame = ttk.Frame(self.root)
        self.name_frame.pack(padx=10, pady=10, anchor="w")
        # Create a label for the search bar
        name_label = ttk.Label(self.name_frame, text="List Name: ")
        name_label.pack(side="left", anchor="w")
        # Create get name bar
        self.get_name = tk.Entry(self.name_frame, highlightthickness=1)
        self.get_name.pack(side="left", fill="x", expand=True, anchor="w")
        self.get_name.focus_set()



        """Display"""
        # Create a frame for the display
        main_display_frame = ttk.Frame(self.root)
        main_display_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Display 1
        self.all_videos_label = ttk.Label(main_display_frame, text="All videos")
        self.all_videos_label.grid(row=0, column=0, sticky="w")

        # Create Treeview
        self.all_videos = ttk.Treeview(main_display_frame, columns=self.columns_video, show="headings")

        # Configure Treeview columns
        self.all_videos.column("Id", width=30, anchor="center")
        self.all_videos.column("Rate", width=70, anchor="center")

        for col in self.columns_video:
            self.all_videos.heading(col, text=col)

        # Add a scrollbar for the Treeview
        self.all_videos_scrollbar = ttk.Scrollbar(main_display_frame, orient="vertical", command=self.all_videos.yview)

        # Configure the Treeview to use the scrollbar
        self.all_videos.configure(yscrollcommand=self.all_videos_scrollbar.set)

        # Place the Treeview and the scrollbar in the grid
        self.all_videos.grid(row=1, column=0, sticky="nsew")
        self.all_videos_scrollbar.grid(row=1, column=1, sticky="ns")

        # Display 2
        self.video_added_label = ttk.Label(main_display_frame, text="Video Added")
        self.video_added_label.grid(row=0, column=3, sticky="w")

        # Create Treeview
        self.video_added = ttk.Treeview(main_display_frame, columns=self.columns_video, show="headings")

        # Configure Treeview columns
        self.video_added.column("Id", width=30, anchor="center")
        self.video_added.column("Rate", width=70, anchor="center")

        for col in self.columns_video:
            self.video_added.heading(col, text=col)

        # Add a scrollbar for the Treeview
        self.video_added_scrollbar = ttk.Scrollbar(main_display_frame, orient="vertical",
                                                   command=self.video_added.yview)

        # Configure the Treeview to use the scrollbar
        self.video_added.configure(yscrollcommand=self.video_added_scrollbar.set)

        # Place the Treeview and the scrollbar in the grid
        self.video_added.grid(row=1, column=3, sticky="nsew")
        self.video_added_scrollbar.grid(row=1, column=4, sticky="ns")

        """BUTTONS"""
        # Create add button
        self.add_btn = ttk.Button(main_display_frame, text="Add Video", compound="left",
                                  command=None)
        # Change column and row parameters to place it between two Treeviews
        self.add_btn.grid(row=1, column=2, sticky="n", padx=10)

        # Create delete button
        self.del_btn = ttk.Button(main_display_frame, text="Remove Video", compound="left",
                                  command=None)
        # Change column and row parameters to place it between two Treeviews
        self.del_btn.grid(row=1, column=2, sticky="s", padx=10)



        # Create create button
        self.create_btn = ttk.Button(self.root, text="Save", compound="left", command=None)
        self.create_btn.pack(side="right", padx=10, pady=10)
if __name__ == "__main__":
    # Create a themed window with the desired theme name
    window = ThemedTk(theme="arc")
    # Create a style object
    style = ttk.Style(window)

    app = UpdatePlaylist(window)
    window.mainloop()