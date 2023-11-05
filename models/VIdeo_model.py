import pandas as pd
from tkinter import filedialog as fd
from pytube import YouTube
import os
import vlc
from pynput import keyboard, mouse

class Video:
    video_file = os.path.join("..", "data", "video_data.csv")
    video_relative_path = os.path.relpath(video_file)

    video_stored_file = os.path.join("..", "data", "videos_stored")
    video_stored_relative_path = os.path.relpath(video_stored_file)

    def __init__(self, id, title, director, path):
        self.id = id
        self.title = title
        self.director = director
        self.path = path
        self.rate = 0
        self.plays = 0

    @classmethod
    def get_video_data(self):
        df = pd.read_csv(self.video_relative_path)
        all_videos = []

        for index, row in df.iterrows():
            id = row["id"]
            title = row["title"]
            director = row["director"]
            path = row["path"]
            video = Video(id=id, title=title, director=director, path=path)
            all_videos.append(video)

        return all_videos

    @classmethod
    def increase_play(self, video_id):
        df = pd.read_csv(self.video_relative_path)
        try:
            video_id = int(video_id)
            df.loc[df.id == video_id, "plays"] += 1
            self.plays = df.loc[df.id == video_id, "plays"].item()
            # update data
            df.to_csv(self.video_relative_path, index=False)
            return df
        except AttributeError:
            return False

    @classmethod
    def delete_video(self, video_id):
        df = pd.read_csv(self.video_relative_path, header=0)
        # keep rows not have the same id with video_id
        df_new = df[df.id != video_id]
        df_old = df[df.id == video_id]
        # check if there is valid id
        if df_old.empty:
            print("No video with the given id found.")
            return False
        # get path
        path = df_old["path"].values[0]
        # update data
        try:
            df_new.to_csv(self.video_relative_path, index=False)
            os.remove(path)
            return True
        except:
            return False

    @classmethod
    def update_video(self, video_id, video_title, video_director, video_path, video_rate, video_plays):
        df = pd.read_csv(self.video_relative_path, header=0)
        try:
            index = df.index[df.id == video_id][0]
            # update
            df.loc[index, "title"] = video_title
            df.loc[index, "director"] = video_director
            df.loc[index, "path"] = video_path
            df.loc[index, "rate"] = video_rate
            df.loc[index, "plays"] = int(video_plays)

            df.to_csv(self.video_relative_path, index=False)
            return True
        except:
            return False


    def add_video_to_data(self, video_title, video_director, video_path):

        """Data part"""
        df = pd.read_csv(self.video_relative_path, header=0)
        # generate a new id by incrementing the maximum id in the file
        # check if there is any video yet
        if "id" in df.columns and not df['id'].isnull().all():
            new_id = df.id.max() + 1
        else:
            new_id = 1
        print(new_id)
        # create a new row with the given parameters
        new_row = [new_id, video_title, video_director, 0, 0, video_path]
        # append the new row to the end of the dataframe
        df.loc[len(df)] = new_row
        try:
            df.to_csv(self.video_relative_path, index=False)
            return True
        except:
            return False

    def get_video_through_youtube(self, video_title, video_url):
        base_name, ext = os.path.splitext(video_title)
        video_title = os.path.join(base_name + ".mp4")

        try:
            # get URL
            yt = YouTube(video_url)
            # dowload
            stream = yt.streams.get_highest_resolution()
            absolute_path = stream.download(filename=video_title, output_path=self.video_stored_relative_path)
            relative_path = os.path.relpath(absolute_path, start=os.getcwd())
            return relative_path
        except Exception:
            return False


    def choose_file(self):
        filename = fd.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")])
        # Move the selected video file to a new folder
        new_path = os.path.join(self.video_stored_relative_path, os.path.basename(filename))
        return filename, new_path

    def move_file(self, filename, path):
        os.rename(filename, path)

    """@classmethod
    def play_video(self, video_id):
        video_list = self.get_video_data()
        video_path = None
        for video in video_list:
            if video.id == video_id:
                video_path = video.path

        if video_path is None:
            return False

        # create a player object
        player = vlc.MediaPlayer(video_path)



        def on_click(x, y, button, pressed):
            if button == mouse.Button.left and pressed:
                if player.is_playing():
                    player.pause()
                else:
                    player.play()

        def on_press(key):
            if key == keyboard.Key.space:
                if player.is_playing():
                    player.pause()
                else:
                    player.play()

        # Listen to mouse click
        mouse_listener = mouse.Listener(on_click=on_click)
        mouse_listener.start()

        # Listen to space key press
        keyboard_listener = keyboard.Listener(on_press=on_press)
        keyboard_listener.start()

        # Wait for both listeners to stop
        mouse_listener.join()
        keyboard_listener.join()

        player.stop()  # Stops the video"""

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_director(self):
        return self.director

    def get_path(self):
        return self.path

    def get_rate(self):
        df = pd.read_csv(self.video_relative_path)
        try:
            rate = df.loc[df.id == self.id, "rate"].values[0]
        except IndexError:
            return 0
        if not rate:
            rate = 0  # set default
        self.rate = rate
        return self.rate

    def get_plays(self):
        df = pd.read_csv(self.video_relative_path)
        plays = df.loc[df.id == self.id, "plays"].values[0]
        if not plays:
            plays = 0
        self.plays = plays
        return self.plays

