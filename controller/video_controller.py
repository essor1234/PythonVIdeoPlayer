from models.VIdeo_model import Video

class VideoController:
    data = Video.get_video_data()

    def list_video(self):
      video_list = []
      for video in self.data:
        id = video.id
        title = video.title
        director = video.director
        rate = video.get_rate()
        video_list.append([id, title, director, rate])
      return video_list

    def find_video_by_id(self, video_id):
        """can cause rate = 0"""
        video_list = []
        for video in self.data:
          if video_id == video.id:
            video_list.append([video.id, video.title, video.director, video.rate])
        # check if there is video in video_list
        if not video_list:
          return False

        return video_list




    def find_video_by_title(self, video_title):
      """can cause rate = 0"""
      video_list = []
      for video in self.data:
        if video_title == video.title:
          video_list.append([video.id, video.title, video.director, video.rate])
      if not video_list:
        return False

      return video_list


    def find_video_by_director(self, video_director):
      """can cause rate = 0"""
      video_list = []
      for video in self.data:
        if video_director == video.director:
          video_list.append([video.id, video.title, video.director, video.rate])
      # check if there is video in video_list
      if not video_list:
        return False

      return video_list

    def find_video_by_rate(self, video_rate):
      """can cause rate = 0"""
      video_list = []
      for video in self.data:
        if video_rate == video.rate:
          video_list.append([video.id, video.title, video.director, video.rate])
      # check if there is video in video_list
      if not video_list:
        return False

      return video_list

    """check video"""
    def check_video(self, video_id):
      for video in self.data:
        if video_id == video.id:
          return video.title, video.director, video.rate, video.plays

      return False


video_controller = VideoController()