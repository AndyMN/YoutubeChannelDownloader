import os

class YoutubeChannelDownloader:

    def __init__(self, YoutubeVideoFetcher, YoutubeVideoDownloader, YoutubeVideoConverter):
        self.YTvideo_fetcher = YoutubeVideoFetcher
        self.YTvideo_downloader = YoutubeVideoDownloader
        self.YTvideo_converter = YoutubeVideoConverter

    def download_channel(self, channel_name, directory, num_videos=-1):

        video_ids = self.YTvideo_fetcher.fetch_videoids(channel_name)

        if num_videos > 0:
            video_ids = video_ids[0:num_videos]

        for video in video_ids:
            filename = self.YTvideo_downloader.download(video, directory)
            if filename != "NULL":
                conversion_result = self.YTvideo_converter.convert(filename, directory, directory)
                if conversion_result == 0:
                    os.remove(directory + filename)