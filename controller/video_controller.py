from models.VIdeo_model import Video

class VideoController:
    data = Video.get_video_data()

    def list_video(self):
        video_list = []
        for video in self.data:
            video_data = self.data_list_return(video)
            # update the rate from data
            video_data[3] = video.get_rate()
            # append it
            video_list.append(video_data)
        return video_list


    def data_list_return(self, video):
        return [video.id, video.title, video.director, video.rate]

    def find_video(self, video_search, mode):

        mode = mode.lower()
        video_list = []
        # check search type
        if mode == "id":
            for video in self.data:
                if int(video_search) == video.id:
                    video_list.append(self.data_list_return(video))

        elif mode == "rate":
            for video in self.data:
                if int(video_search) == video.rate:
                    video_list.append(self.data_list_return(video))


        elif mode == "title":
            for video in self.data:
                if video_search.lower().replace(" ", "") in video.title.lower().replace(" ", ""):
                    video_list.append(self.data_list_return(video))
        elif mode == "director":
            for video in self.data:
                if video_search.lower().replace(" ", "") in video.director.lower().replace(" ", ""):
                    video_list.append(self.data_list_return(video))
        else:
            return "None"

        # check if have video in video_list
        if not video_list:
            return "None"

        return video_list

    """check video"""
    def check_video(self, video_id):
      for video in self.data:
        if video_id == video.id:
          return video.title, video.director, video.rate, video.plays, video.path

      return False


video_controller = VideoController()