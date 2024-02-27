import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
from ttkthemes import ThemedTk

from models.Playlist_model import Playlist
from controller.playlist_controller import playList_controller
from models.player_model import Player
from models.VIdeo_model import Video


from UI.create_playlist import CreatePlaylist
from UI.update_playlist import UpdatePlaylist

class PlaylistManager(tk.Frame):
    columns = ["Id", "Title", "Length"]
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent= parent
        self.video_queue = []
        # window display
        self.root = self.parent
        self.root.title("Playlist Manager")
        self.top_open = False

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
        btn_check_video = ttk.Button(self.search_frame, text="REFRESH", compound="left",
                                     command= self.refresh)
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
                                  command=lambda: self.create_window())
        self.add_btn.grid(row=0, column=0, ipady=20, ipadx=20)
        # update button
        self.update_btn = ttk.Button(self.function_btn_frame, text="Update Playlist", compound="left",
                                  command=  self.combine)
        self.update_btn.grid(row=1, column=0, ipady=5, ipadx=5, padx=10, pady=10)
        # delete button
        self.delete_btn = ttk.Button(self.function_btn_frame, text="Delete Playlist", compound="left",
                                     command= self.delete_func)
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
        self.play_btn = ttk.Button(self.listbox_frame, text="PLay", width=70, command= self.play_video)
        self.play_btn.grid(row=3, column=0, padx=10, pady=10)

        self.list_all()
        self.search_entry.bind('<Return>', self.search_video)
        self.main_display.bind('<Double-Button-1>', self.check_list)

    def create_window(self):
        if not self.top_open:
            self.top_open = True
            new_window = tk.Toplevel(self)
            frame = CreatePlaylist(new_window, self)
            frame.pack()
            new_window.protocol("WM_DELETE_WINDOW", lambda: self.close_top(new_window))

    def update_window(self):
        print(self.top_open)
        if not self.top_open:
            self.top_open = True
            new_window = tk.Toplevel(self)
            frame = UpdatePlaylist(new_window, self)
            frame.pack()
            new_window.protocol("WM_DELETE_WINDOW", lambda: self.close_top(new_window))

    def close_top(self, window):
        self.top_open = False
        window.destroy()

    def set_top_open_false(self):
        self.top_open = False


    def info_for_chosen_list(self):
        try:
            item_id = self.main_display.focus()

            # get id and title of list
            item = self.main_display.item(item_id, "values")
            try:
                list_id = int(item[0])
                list_title = item[1]
            except ValueError:
                list_id = -1
                list_title = "None"
            return list_id, list_title
        except IndexError:
            warning_label = tk.Label(self.search_frame, text="PLease choose a list to optimize", fg="red")
            warning_label.grid(row=1, column=1)
            warning_label.after(1000, warning_label.destroy)

    # allow using 2 function in the same button
    def combine(self):
        self.update_window()
        self.info_for_chosen_list()

    # def video_in_list_display(self, event):
    #     self.main_display.delete(*self.main_display.get_children())
    #     # get the selected item from the event widget
    #     item_id = event.widget.focus()
    #     item = event.widget.item(item_id, "values")
    #     try:
    #         list_id = item[0]
    #     except ValueError:
    #         list_id = -1
    #
    #     try:
    #         for video in controller.display_videos_in_list(list_id):
    #             self.video_display.insert("", "end", values=(video[0], video[1], video[2], "*" * int(video[3])))
    #     except TypeError:
    #         item_id = self.video_display.insert("", "end", values=("", "", "", ""))
    #         self.video_display.set(item_id, column="Title", value="None")
    #     for video in controller.display_videos_in_list(list_id):
    #         self.video_display.insert("", "end", values=(video[0], video[1], video[2], "*" * int(video[3])))

    def list_all(self):
        # Remove every children from the display
        for i in self.main_display.get_children(): # return a list of child of objects on main_display
            self.main_display.delete(i) # remove that list from the display
            # For each data, add a new row to the display
        for item in playList_controller.list_playlist(): # For each data
            self.main_display.insert("", "end", values=(item[0], item[1], item[2])) # add a new row to the display

    def delete_func(self):
        seleted_item = self.main_display.focus()
        if not seleted_item:
            """TODO: create warning later"""
            return False
        # get video id
        try:
            list_id = int(self.main_display.item(seleted_item, "values")[0])
        except ValueError:
            list_id = -1
        # call delete method
        is_deleted = Playlist.delete_list(list_id)
        # check if video is deleted in data or not
        if is_deleted:
            self.main_display.delete(seleted_item)

    def search_video(self, event):
        search_value = self.search_entry.get()
        selected_mode = self.search_combobox.get()
        # clear treview
        self.main_display.delete(*self.main_display.get_children())
        if not search_value:
            """ return warning later"""
            return False

        try:
            for video in playList_controller.find_list(search_value, selected_mode):
                self.main_display.insert("", "end", values=(video[0], video[1], video[2]))
        except TypeError:
            """ return warning later"""
            return "False"
        except ValueError:
            return "False"
        except IndexError:
            return "False"

    '''
    Need search function
    play function 
    display all video names in the list into a sub display(maybe add a thumbnail into it too)
    '''
    def refresh(self):
        self.main_display.delete(*self.main_display.get_children())
        self.list_all()
        self.listbox.delete(0, tk.END)
        playList_controller.refresh_data()

    def check_list(self, event):
        # videos = []
        # # get video_id from treeview (in a tuple)
        # list_id = self.main_display.selection()
        # # clear list box
        # self.listbox.delete(0, tk.END)
        #
        # for video_id in list_id:
        #     values = self.main_display.item(video_id, "values")
        #     try:
        #         video_key = int(values[0])
        #     except IndexError:
        #         return False
        #
        #     # if playList_controller.display_video_in_list(video_key) == False:
        #     #     break
        #     # run method
        #     videos = playList_controller.display_video_in_list(video_key)
            # insert video into list box
        list_id, list_title = self.info_for_chosen_list()
        self.listbox.delete(0, tk.END)

        try:
            order = 0
            for video in playList_controller.display_video_in_list(list_id):
                order += 1
                self.listbox.insert(tk.END, order)
                self.listbox.insert(tk.END, "Title: " + video[1])
                self.listbox.insert(tk.END, "Director: " + video[2])
                self.listbox.insert(tk.END, "Rate: " + str(video[3]))
                self.listbox.insert(tk.END, "=" * 100, " ")
        except TypeError:
            self.listbox.insert(tk.END, "")
            # self.get_current_name.insert(0, list_title)

    # def play_video(self):
    #     # store full info of video in list
    #     video_in_list = []
    #     # All videos in database
    #     all_video = Video.get_video_data()
    #     # Videos in a list
    #     list_id, list_title = self.info_for_chosen_list()
    #     for video_inside_list in playList_controller.display_video_in_list(list_id):
    #         for videos in all_video:
    #             if videos.id == video_inside_list[0]:
    #                 video_in_list.append((videos.id, videos.path))
    #
    #
    #
    #
    #     for video_id, video_path in video_in_list:
    #         print(f"Video path: {video_path} \nVideo id: {video_id}")
    #
    #         new_window = tk.Toplevel(self)
    #         frame = Player(new_window, video_path, title="tkinter vlc")
    #
    #         def close_window_and_stop_player():
    #             frame.stop()
    #             new_window.destroy()
    #
    #         new_window.protocol("WM_DELETE_WINDOW", close_window_and_stop_player)
    #         new_window.mainloop()



    # def return_video_path(self, video):
    #     video_id = video.id
    #     video_path = video.path
    #
    #     if video_path is None:
    #         return False
    #
    #     return video_path, video_id

    def add_to_queue(self, video_list):
        for video in video_list:
            self.video_queue.append(video)

    def play_next_video(self):
        if self.video_queue:  # if there are videos left in the queue
            video_id, video_path = self.video_queue.pop(0)  # get the next video
            print(f"Video path: {video_path} \nVideo id: {video_id}")

            new_window = tk.Toplevel(self.main_display)
            frame = Player(new_window, video_path, title="tkinter vlc")
            Video.increase_play(video_id)

            def close_window_and_stop_player():
                frame.stop()
                new_window.destroy()
                self.play_next_video()  # play the next video

            new_window.protocol("WM_DELETE_WINDOW", close_window_and_stop_player)
            new_window.mainloop()
        else:
            print("No more videos in the queue.")

    def play_video(self):
        video_in_list = []
        # All videos in database
        all_video = Video.get_video_data()
        # Videos in a list
        list_id, list_title = self.info_for_chosen_list()
        for video_inside_list in playList_controller.display_video_in_list(list_id):
            for videos in all_video:
                if videos.id == video_inside_list[0]:
                    video_in_list.append((videos.id, videos.path))
        self.add_to_queue(video_in_list)
        self.play_next_video()

# if __name__ == "__main__":
#     # Create a themed window with the desired theme name
#     window = ThemedTk(theme="arc")
#     # Create a style object
#     style = ttk.Style(window)
#
#
#     app = PlaylistManager(window, None)
#     app.grid()
#     window.mainloop()