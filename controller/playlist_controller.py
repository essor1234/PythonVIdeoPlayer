from models.Playlist_model import Playlist
from models.VIdeo_model import Video

class PlaylistController:
    data = Playlist.get_playlist_data()
    video_data = Video.get_video_data()

    def refresh_data(self):
        self.data = Playlist.get_playlist_data()

    def list_playlist(self):
        playlist_list = []
        for playlist in self.data:
            id = playlist.id
            title = playlist.title
            length = playlist.get_length()
            playlist_list.append([id, title, length])
        return playlist_list


    def find_list_by_id(self, list_id):
        playlist_list = []
        for playlist in self.data:
            if list_id == playlist.id:
                playlist_list.append([playlist.id, playlist.title, playlist.length])

        if playlist_list is None:
            return False

        return playlist_list


    def find_list_by_title(self, list_title):
        playlist_list = []
        for playlist in self.data:
            if list_title == playlist.title:
                playlist_list.append([playlist.id, playlist.title, playlist.length])

        if playlist_list is None:
            return False

        return playlist_list

    def find_list(self, list_search, mode):
        mode = mode.lower()
        lists = []
        if mode == "id":
            for playlist in self.data:
                print(list_search)
                print(playlist.id)
                if list_search == playlist.id:
                    lists.append([playlist.id, playlist.title, playlist.length])
        elif mode == "title":
            for playlist in self.data:
                if list_search.lower().replace(" ", "") in playlist.title.lower().replace(" ", ""):
                    lists.append([playlist.id, playlist.title, playlist.length])

        if lists is None:
            return False
        print(lists)
        return lists


    def display_video_in_list(self, list_id):
        video_list = []
        for playlist in self.data:
            if list_id == playlist.id:
                video_ids = [int(id) for id in str(playlist.get_video_ids()).split(", ")]
                for id_video in video_ids:
                    for video in self.video_data:
                        if id_video == video.id:  # Compare id_video with video.id
                            video_list.append([video.id, video.title, video.director, video.rate])

        return video_list


playList_controller = PlaylistController()