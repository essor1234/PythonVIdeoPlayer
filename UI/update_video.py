import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

from models.VIdeo_model import Video
class UpdateVideo(tk.Frame, Video):
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
        self.get_path_lbl = ttk.Label(self.get_frame, text="Path: ")
        self.get_path_lbl.grid(row=3, column=0, padx=5, pady=5)
        # path entry
        self.get_path = tk.Entry(self.get_frame, highlightthickness=1)
        self.get_path.grid(row=3, column=1, columnspan=3, sticky="w", padx=5, pady=5)



        # plays label
        self.get_plays_lbl = ttk.Label(self.get_frame, text="Plays: ")
        self.get_plays_lbl.grid(row=4, column=0, padx=5, pady=5)
        # plays listbox
        self.get_plays = tk.Listbox(self.get_frame, height=1, width=10)
        self.get_plays.grid(row=4, column=1, columnspan=3, sticky="w", padx=5, pady=5)

        # plays reset button
        self.reset_btn = ttk.Button(self.get_frame, text="Reset",
                                    command=self.reset_play)
        self.reset_btn.grid(row=4, column=2, columnspan=3, padx=5, pady=5)


        # save button
        self.save_btn = ttk.Button(self.root, text="Save",
                                   command=self.save_function)
        self.save_btn.config(width=50)
        self.save_btn.grid(columnspan=3, padx=5, pady=5)

        self.get_video_info()
    def get_video_info(self):
        video_title, video_director, video_rate, video_plays, video_path, video_id = self.update_video.info_for_chosen_video()
        self.get_title.insert(0, video_title)
        self.get_director.insert(0, video_director)
        self.get_rate.insert(0, video_rate)
        self.get_path.insert(0, video_path)
        self.get_plays.insert(tk.END, video_plays)


    def reset_play(self):
        self.get_plays.delete(0, tk.END)
        self.get_plays.insert(tk.END, 0)

    def save_function(self):
        video_title, video_director, video_rate, video_plays, video_path, video_id = self.update_video.info_for_chosen_video()
        current_title = self.get_title.get()
        current_director = self.get_director.get()
        current_rate = self.get_rate.get()
        current_path = self.get_path.get()
        current_play = self.get_plays.get(tk.ACTIVE)
        try:
            current_rate = int(current_rate)
        except (TypeError, ValueError):
            """ TODO: warning feature later"""
            return False

        if not current_title:
            return False

        elif not current_director:
            return False
        elif not current_path:
            return False

        elif not current_rate or current_rate > 5:
            if not self.warning_shown:
               return False
        else:
            Video.update_video(video_id, current_title, current_director, current_path, current_rate, current_play)
            self.root.destroy()




if __name__ == "__main__":
    # Create a themed window with the desired theme name
    window = ThemedTk(theme="arc")
    # Create a style object
    style = ttk.Style(window)


    app = UpdateVideo(window, None)
    window.mainloop()