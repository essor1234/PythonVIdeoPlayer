import pandas as pd
import os

class Playlist:
    playlist_file = "../data/playlist_data.csv"
    playlist_relative_path = os.path.relpath(playlist_file)

    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.length = 0
        self.video_ids = []

    @classmethod
    def get_playlist_data(self):
        df = pd.read_csv(self.playlist_relative_path, header=0)
        all_playlist = []

        for index, row in df.iterrows():
            id = row["id"]
            title = row["title"]
            playlist = Playlist(id=id, title=title)
            all_playlist.append(playlist)
        return all_playlist

    def create_list(self, list_title, video_ids):
        self.video_ids.append(video_ids)
        df = pd.read_csv(self.playlist_relative_path, header=0)
        length = len(video_ids.split(", "))
        # generate a new id by incrementing the maximum id in the file
        new_id = df.id.max() + 1 if df.id.max() >= 0 else 1
        self.id = new_id  # assign the new id to the Playlist object
        # create a new row with the given parameters
        new_row = [new_id, list_title, video_ids, length]
        # append the new row to the end of the dataframe
        df.loc[len(df)]= new_row
        try:
            df.to_csv(self.playlist_file, index=False)
            return True
        except:
            return False

    def update_list(self, list_id, list_title, video_ids):
        # Ensure video_ids are valid
        video_ids = [vid.strip() for vid in video_ids.split(",") if vid.strip().isdigit()]

        df = pd.read_csv(self.playlist_file, header=0)
        # get index
        index = df.index[df.id == list_id][0]
        # update
        df.loc[index, "title"] = list_title
        df.loc[index, "video_id"] = ', '.join(map(str, video_ids))
        df.loc[index, "length"] = len(video_ids)
        try:
            df.to_csv(self.playlist_file, index=False)
            return True
        except:
            return False

    def delete_list(self, list_id):
        df = pd.read_csv(self.playlist_file, header=0)
        # keep row have different id
        df = df[df.id != list_id]
        try:
            df.to_csv(self.playlist_file, index=False)
            return True
        except:
            return False

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_length(self):
        df = pd.read_csv(self.playlist_relative_path)
        length = df.loc[df.id == self.id, "length"].values[0]
        self.length = length
        return self.length

    def get_video_ids(self):
        df = pd.read_csv(self.playlist_relative_path)
        video_ids = df.loc[df.id == self.id, "video_id"].values[0]
        self.video_ids = video_ids
        return self.video_ids


