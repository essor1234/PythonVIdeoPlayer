

class Playlist:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.length = 0
        self.video_ids = []

    def get_playlist_data(self):
        pass

    def create_list(self, list_title, video_ids):
        pass

    def update_list(self, list_id, list_title, video_ids):
        pass

    def play_list(self, list_id):
        pass

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_length(self):
        return self.length

    def get_video_ids(self):
        return self.video_ids