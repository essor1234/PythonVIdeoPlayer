import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
from ttkthemes import ThemedTk

from controller.video_controller import video_controller
from models.VIdeo_model import Video
class VideoManager(tk.Frame):
    columns = ["Id", "Title", "Director", "Rate"]
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.parent= parent
        # window display
        self.root = self.parent
        self.root.title("Video Manager")

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
        btn_check_video = ttk.Button(self.search_frame, text="Search", compound="left",
                                     command=None)
        btn_check_video.config(width=15)
        btn_check_video.grid(row=0, column=3)

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
                                  command=None)
        self.add_btn.grid(row=0, column=0, ipady=20, ipadx=20)
        # update button
        self.update_btn = ttk.Button(self.function_btn_frame, text="Update Video", compound="left",
                                  command=None)
        self.update_btn.grid(row=1, column=0, ipady=5, ipadx=5, padx=10, pady=10)
        # delete button
        self.delete_btn = ttk.Button(self.function_btn_frame, text="Delete Video", compound="left",
                                     command=None)
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

        """Play button"""
        self.play_btn = ttk.Button(self.listbox_frame, text="PLay", width=70)
        self.play_btn.grid(row=3, column=0, padx=10, pady=10)


    def check_video(self):
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
            video_title, video_director, video_rate, video_plays = video_controller.check_video(video_key)
            # insert video into list box
            self.listbox.insert(tk.END, video_title)
            self.listbox.insert(tk.END, video_director)
            self.listbox.insert(tk.END, "Rate: " + str(video_rate))
            self.listbox.insert(tk.END, "PLays: " + str(video_plays))

    def update_video(self):
        pass

    def add_video(self):
        pass

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



    def play_video(self):
        selected_item = self.main_display.focus()
        # check if is there selected_item or not
        if not selected_item:
            """TODO: create warning later"""
            return False

        try:
            video_id = int(self.main_display.item(selected_item, "values")[0])
        except ValueError:
            video_id = -1
        # play video chosen
        Video.play_video(video_id)
        # increase play count
        Video.increase_play(video_id)



    def search_video(self, selected_mode):
        search_value = self.search_entry.get()
        # clear treview
        self.main_display.delete(*self.main_display.get_children())
        if not search_value:
            """ return warning later"""
            return False

        # choose mode part
        if selected_mode == "Title":
            try:
                for video in video_controller.find_video_by_title(search_value):
                    self.main_display.insert("", "end", values=(video[0], video[1]. video[2], "*" * int(video[3])))
            except TypeError:
                """ return warning later"""
                return False

        elif selected_mode == "Director":
            try:
                for video in video_controller.find_video_by_director(search_value):
                    self.main_display.insert("", "end", values=(video[0], video[1]. video[2], "*" * int(video[3])))
            except TypeError:
                """ return warning later"""
                return False

        elif selected_mode == "Id":
            try:
                for video in video_controller.find_video_by_id(int(search_value)):
                    self.main_display.insert("", "end", values=(video[0], video[1].video[2], "*" * int(video[3])))
            except ValueError:
                return False
            except IndexError:
                return False

        elif selected_mode == "Rate":
            try:
                for video in video_controller.find_video_by_id(int(search_value)):
                    self.main_display.insert("", "end", values=(video[0], video[1].video[2], "*" * int(video[3])))
            except ValueError:
                return False
            except IndexError:
                return False




if __name__ == "__main__":
    # Create a themed window with the desired theme name
    window = ThemedTk(theme="arc")
    # Create a style object
    style = ttk.Style(window)


    app = VideoManager(window, None)
    app.pack()
    window.mainloop()