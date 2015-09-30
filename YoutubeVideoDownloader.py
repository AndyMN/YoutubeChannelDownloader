import os
import glob
from pytube import YouTube

class YoutubeVideoDownloader:

    def __init__(self):
        self.youtube = YouTube()

    def download(self, video_id, directory, video_quality="mp4"):
        if not os.path.isdir(directory):
            os.makedirs(directory)

        try:
            youtube_url ="https://www.youtube.com/watch?v=%s" % video_id
            self.youtube.url = youtube_url
            youtube_video = self.youtube.get(video_quality)
            video_name = self.youtube.filename
            filename = video_name + ".%s" % video_quality
            if not glob.glob(directory + video_name + ".*"): #Check to see if the file was already downloaded or not
                youtube_video.download(directory)
                return filename
            else:
                print "Already downloaded: %s" % filename
                return filename
        except:
            print "Failed to download: %s" % filename
            return "NULL"
            pass