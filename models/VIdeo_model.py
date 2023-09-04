import pandas as pd
from tkinter import filedialog as fd
from pytube import YouTube
import os


class Video:
    video_file = "../data/video_data.csv"
    video_relative_path = os.path.relpath(video_file)

    video_stored_file = "..data/videos_stored"
    video_stored_relative_path = os.path.relpath(video_stored_file)

    def __init__(self, id, title, director, path):
        self.id = id
        self.title = title
        self.director = director
        self.path = path
        self.rate = 0
        self.plays = 0

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

    def increase_play(self, video_id):
        df = pd.read_csv(self.video_relative_path)
        try:
            video_id = int(video_id)
            df.loc[df.id == video_id, "plays"] += 1
            self.plays = df.loc[df.id == video_id, "plays"].item()
            df.to_csv(self.video_relative_path, index=False)
            return df
        except AttributeError:
            return False

    def delete_video(self, video_id):
        df = pd.read_csv(self.video_relative_path, header=0)
        # keep rows not have the same id with video_id
        df = df[df.id != video_id]
        try:
            df.to_csv(self.video_relative_path, index=False)
            return True
        except:
            return False

    def update_video(self, video_id, video_title, video_director, video_path, video_rate, video_plays):
        df = pd.read_csv(self.video_relative_path, header=0)
        try:
            index = df.index[df.id == video_id][0]
            # update
            df.loc[index, "title"] = video_title
            df.loc[index, "director"] = video_director
            df.loc[index, "path"] = video_path
            df.loc[index, "rate"] = video_rate
            df.loc[index, "plays"] = video_plays

            df.to_csv(self.video_relative_path, index=False)
            return True
        except:
            return False


    def add_video_to_data(self, video_title, video_director, video_path):

        """Data part"""
        df = pd.read_csv(self.video_relative_path, header=0)
        # generate a new id by incrementing the maximum id in the file
        new_id = df.id.max()+1
        # create a new row with the given parameters
        new_row = [new_id, video_title, video_director, self.rate, self.plays, video_path]
        # append the new row to the end of the dataframe
        df.loc[len(df)] = new_row


    def get_video_through_youtube(self, video_title, video_url):
        video_title += ".mp4"
        try:
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            stream.download(filename=video_title)
            path = stream.download(output_path=self.video_stored_relative_path)
            return path
        except Exception:
            return False


    def get_video_through_device(self):
        """Video part"""
        # Show a file dialog that only accepts video files
        filename = fd.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")])
        # Move the selected video file to a new folder
        path = os.rename(filename, self.video_stored_relative_path + "/" + os.path.basename(filename))
        return path

    def play_video(self, video_id):
        pass

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_director(self):
        return self.director

    def get_path(self):
        return self.path

    def get_rate(self):
        return self.rate

    def get_plays(self):
        return self.plays