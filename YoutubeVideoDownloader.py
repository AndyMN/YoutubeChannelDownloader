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
            self.youtube.from_url(youtube_url)
            youtube_video = self.youtube.filter(video_quality)[-1]
            video_name = self.youtube.filename
            filename = video_name + ".%s" % video_quality
            if not glob.glob(directory + video_name + ".*"): #Check to see if the file was already downloaded or not
                print "Downloading: %s" % filename
                youtube_video.download(directory)
                return filename
            else:
                print "Already downloaded: %s" % filename
                return filename
        except Exception as e:
            print str(e)
            print "Failed to download: %s" % youtube_url
            return "NULL"
            pass