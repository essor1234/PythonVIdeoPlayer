import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont


from controller.video_controller import video_controller
from models.VIdeo_model import Video
from models.player_model import Player


from UI.add_video import AddVideo
from UI.update_video import UpdateVideo
class VideoManager(tk.Frame):
    columns = ["Id", "Title", "Director", "Rate"]


    def __init__(self, parent):
        tk.Frame.__init__(self, parent)


        self.parent= parent
        # window display
        self.root = self.parent
        self.root.title("Video Manager")
        self.top_open = False
        self.pack(fill='both', expand=True)

        """Warning area"""
        # Create a style object
        self.title_frame = ttk.Labelframe(self, borderwidth=0, relief="flat")
        self.title_frame.grid(row=0, column=1, padx=5, pady=5, sticky="N")
        my_font = tkfont.Font(family="Arial", size=20)
        # Create a label with the custom font and no border
        label = ttk.Label(self.title_frame, text="Welcome to Video Manager", font=my_font, borderwidth=0)
        label.grid(row=0, column=0, sticky="N")

        """Setting buttons"""
        self.function_btn_frame = ttk.Frame(self, relief="ridge", borderwidth=5)
        self.function_btn_frame.grid(row=0, column=0, padx=5, pady=5, sticky="W")
        # add button
        self.add_btn = ttk.Button(self.function_btn_frame, text="Add Video", compound="left",
                                  command=self.add_video)
        self.add_btn.grid(row=0, column=0, ipady=20, ipadx=20)
        # update button
        self.update_btn = ttk.Button(self.function_btn_frame, text="Update Video", compound="left",
                                    command=self.update_video)
        self.update_btn.grid(row=1, column=0, ipady=5, ipadx=5, padx=10, pady=10)
        # delete button
        self.delete_btn = ttk.Button(self.function_btn_frame, text="Delete Video", compound="left",
                                     command=self.delete_video)
        self.delete_btn.grid(row=2, column=0, ipady=5, ipadx=5, padx=10, pady=10)

        """Display"""
        self.main_display = ttk.Treeview(self.title_frame, columns=self.columns, show="headings")
        self.main_display.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.main_display.column("Id", width=30, anchor="center")
        self.main_display.column("Rate", width=70, anchor="center")

        # Configure Treeview columns
        for col in self.columns:
            self.main_display.heading(col, text=col)


        self.listbox_frame = ttk.Frame(self)
        self.listbox_frame.grid(row=0, column=3, rowspan=2, padx=10, pady=10)
        # Create Listbox widget
        self.listbox = tk.Listbox(self.listbox_frame, height=12, width=60)
        self.listbox.grid(row=1, column=0, rowspan=2, padx=10, pady=10)

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
        search_options = ["Title", "Director", "Rate", "Id"]
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
                                     command=lambda: self.refresh())
        btn_check_video.config(width=15)
        btn_check_video.grid(row=0, column=3)

        """Play button"""
        self.play_btn = ttk.Button(self.listbox_frame, text="PLay", width=70,
                                   command=self.play_video)
        self.play_btn.grid(row=3, column=0, padx=10, pady=10)


        self.list_all()
        self.main_display.bind('<Double-Button-1>', self.check_video)
        self.search_entry.bind('<Return>', self.search_video)

    def populate_listbox(self, listbox):
        listbox.delete(0, tk.END)
        for video in video_controller.data:
            listbox.insert(tk.END, video.title)

    def refresh(self):
        self.main_display.delete(*self.main_display.get_children())
        self.list_all()
        self.listbox.delete(0, tk.END)
        video_controller.refresh_data()

    def list_all(self):
        for video in video_controller.list_video():
            self.main_display.insert("", "end", values=(video[0], video[1], video[2], "*" * int(video[3])))
    def check_video(self, event):
        # get video_id from treeview (in a tuple)
        video_ids = self.main_display.selection()
        # clear list box
        self.listbox.delete(0, tk.END)

        for video_id in video_ids:
            values = self.main_display.item(video_id, "values")
            try:
                video_key = int(values[0])
            except IndexError:
                return False

            if video_controller.check_video(video_key) == False:
                break
            # run method
            video_title, video_director, video_rate, video_plays, video_path = video_controller.check_video(video_key)
            # insert video into list box
            self.listbox.insert(tk.END, video_title)
            self.listbox.insert(tk.END, video_director)
            self.listbox.insert(tk.END, "Rate: " + str(video_rate))
            self.listbox.insert(tk.END, "PLays: " + str(video_plays))

    def info_for_chosen_video(self):
        try:
            get_video = self.main_display.focus()
            # get id
            video = self.main_display.item(get_video, "values")
            try:
                video_id = int(video[0])
            except ValueError:
                video_id = -1
            # run method
            video_title, video_director, video_rate, video_plays, video_path = video_controller.check_video(video_id)
            return video_title, video_director, video_rate, video_plays, video_path, video_id
        except IndexError:
            return False
    def update_video_window_display(self):
        get_video = self.main_display.focus()
        if get_video:
            if not self.top_open:
                self.top_open = True
                # create a Toplevel widget
                new_window = tk.Toplevel(self)
                # create a CheckVideo frame inside the new window
                check_video_frame = UpdateVideo(new_window, self)
                # create name
                check_video_frame.grid()
                new_window.protocol("WM_DELETE_WINDOW", lambda: self.close_top(new_window))

    def update_video(self):
        self.info_for_chosen_video()
        self.update_video_window_display()
        self.main_display.selection_remove(self.main_display.selection()[0])
        self.top_open=False

    def add_video(self):
        # Access the global flag variable
        # Check if the flag is False, meaning no Toplevel window is open
        if not self.top_open:
            self.top_open = True
            new_window = tk.Toplevel(self)
            frame = AddVideo(new_window)
            frame.grid()
            new_window.protocol("WM_DELETE_WINDOW", lambda: self.close_top(new_window))

    def delete_video(self):
        seleted_item = self.main_display.focus()
        if not seleted_item:
            """TODO: create warning later"""
            return False
        #get video id
        try:
            video_id = int(self.main_display.item(seleted_item, "values")[0])
        except ValueError:
            video_id= -1
        # call delete method
        is_deleted = Video.delete_video(video_id)
        # check if video is deleted in data or not
        if is_deleted:
            self.main_display.delete(seleted_item)



    def return_video_path(self):

        selected_item = self.main_display.focus()
        # check if is there selected_item or not
        if not selected_item:
            """TODO: create warning later"""
            return False

        try:
            video_id = int(self.main_display.item(selected_item, "values")[0])
        except ValueError:
            video_id = -1

        video_list = Video.get_video_data()
        video_path = None
        for video in video_list:
            if video.id == video_id:
                video_path = video.path

        if video_path is None:
            return False

        return video_path, video_id

        # play video chosen
        # Create a Qt Application

    def play_video(self):
        video_path, video_id = self.return_video_path()
        print(f"Video path: {video_path} \nVideo id: {video_id}")

        new_window = tk.Toplevel(self)
        frame = Player(new_window, video_path, title="tkinter vlc")
        Video.increase_play(video_id)

        def close_window_and_stop_player():
            frame.stop()
            new_window.destroy()

        new_window.protocol("WM_DELETE_WINDOW", close_window_and_stop_player)
        new_window.mainloop()




    def search_video(self, event):
        search_value = self.search_entry.get()
        selected_mode = self.search_combobox.get()
        # clear treview
        self.main_display.delete(*self.main_display.get_children())
        if not search_value:
            """ return warning later"""
            return False

        try:
            for video in video_controller.find_video(search_value, selected_mode):
                self.main_display.insert("", "end", values=(video[0], video[1], video[2], "*" * int(video[3])))
        except TypeError:
            """ return warning later"""
            return "False"
        except ValueError:
            return "False"
        except IndexError:
            return "False"

    # use for prevent multiple instances
    def close_top(self, top_window):
        self.top_open = False
        # Destroy the Toplevel window
        top_window.destroy()


if __name__ == "__main__":
    # Create a themed window with the desired theme name
    window = tk.Tk()
    # Create a style object
    app = VideoManager(window)
    window.mainloop()