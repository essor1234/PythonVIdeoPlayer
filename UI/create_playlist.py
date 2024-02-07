import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

from controller.video_controller import video_controller
from models.VIdeo_model import Video
from models.Playlist_model import Playlist


class CreatePlaylist(tk.Frame):
    columns_video = ["Id", "Title", "Director", "Rate"]

    def __init__(self, parent, playlist_manager):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.warning_shown = False
        # window display
        self.root = self.parent
        self.root.title("Create Playlist")
        self.playlist_manager = playlist_manager

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
        btn_check_video = ttk.Button(self.search_frame, text="REFRESH", compound="left",
                                     command= self.refresh)
        btn_check_video.config(width=15)
        btn_check_video.grid(row=0, column=3, padx=5, pady=5)
        self.search_entry.bind('<Return>', self.search_video)



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
                                  command= self.add_video)
        # Change column and row parameters to place it between two Treeviews
        self.add_btn.grid(row=1, column=2, sticky="n", padx=10)

        # Create delete button
        self.del_btn = ttk.Button(main_display_frame, text="Remove Video", compound="left",
                                  command= self.remove_video)
        # Change column and row parameters to place it between two Treeviews
        self.del_btn.grid(row=1, column=2, sticky="s", padx=10)



        # Create create button
        self.create_btn = ttk.Button(self.root, text="Create", compound="left", command= self.create_func)
        self.create_btn.pack(side="right", padx=10, pady=10)

        """Display videos"""
        self.display_video()


    def display_video(self):
        # Remove all videos on the display
        for i in self.all_videos.get_children():
            self.all_videos.delete(i)
        for video in video_controller.list_video():
            self.all_videos.insert("", "end", values=
                                (video[0], video[1], video[2], "*" * video[3]))

    def add_video(self):
        try:
            # Get the selected item ID from the source treeview
            selected_item = self.all_videos.selection()[0]
        except IndexError:
            return None
        # Get the values of the selected item
        values = self.all_videos.item(selected_item)["values"]
        # Get the video ID from the first value
        video_id = int(values[0])
        video_title, video_director, video_rate, rate, path = video_controller.check_video(video_id)
        # Insert the values into the destination treeview
        self.video_added.insert("", "end", values=(video_id, video_title, video_director, "*" * video_rate))
        # Delete the selected item from the source treeview
        self.all_videos.delete(selected_item)

    def remove_video(self):
        try:
            # Get the selected item ID from the source treeview
            selected_item = self.video_added.selection()[0]
        except IndexError:
            return None
        # Get the values of the selected item
        values = self.video_added.item(selected_item)["values"]
        # Get the video ID from the first value
        video_id = int(values[0])
        video_title, video_director, video_rate, rate, path = video_controller.check_video(video_id)
        # Insert the values into the destination treeview
        self.all_videos.insert("", "end", values=(video_id, video_title, video_director, "*" * video_rate))
        # Delete the selected item from the source treeview
        self.video_added.delete(selected_item)

    """TODO: Need to find a solution to use playlist_model file."""
    def create_func(self):
        video_list = []
        list_name = self.get_name.get()

        for line in self.video_added.get_children():
            video = self.video_added.item(line)["values"]
            video_list.append(str(video[0]))

        video_list = ", ".join(video_list)

        if not list_name:
            self.get_name.config(highlightbackground="red", highlightcolor="red")
            if not self.warning_shown:
                warning_label = tk.Label(self.name_frame, text="Name is required!", fg="red")
                warning_label.pack()
                self.warning_shown = True
            # change the color of the entry widget
        else:
            # do something with list_name and video_list
            playlist_model = Playlist(list_name, video_list)
            playlist_model.create_list(list_name, video_list)
            # destroy the window
            self.root.destroy()
            self.playlist_manager.set_top_open_false()

    def search_video(self, event):
        search_value = self.search_entry.get()
        selected_mode = self.search_combobox.get()
        # clear treeview
        self.all_videos.delete(*self.all_videos.get_children())
        if not search_value:
            """ return warning later"""
            return False

        try:
            for video in video_controller.find_video(search_value, selected_mode):
                self.all_videos.insert("", "end", values=(video[0], video[1], video[2], "*" * int(video[3])))
        except TypeError:
            """ return warning later"""
            return "False"
        except ValueError:
            return "False"
        except IndexError:
            return "False"

    def refresh(self):
        """
        Optional: Might need to fix problem for appear added video after refresh
        :return:
        """
        self.all_videos.delete(*self.all_videos.get_children())
        self.display_video()
        # self.listbox.delete(0, tk.END)
        video_controller.refresh_data()

# if __name__ == "__main__":
#     # Create a themed window with the desired theme name
#     window = ThemedTk(theme="arc")
#     # Create a style object
#     style = ttk.Style(window)
#
#     app = CreatePlaylist(window)
#     window.mainloop()