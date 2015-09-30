from PrivateVars import APIkey
from YoutubeVideoFetcher import YoutubeVideoFetcher
from YoutubeVideoDownloader import YoutubeVideoDownloader
from VideoConverter import VideoConverter
from YoutubeChannelDownloader import YoutubeChannelDownloader

channel_name = raw_input("What channel to download from ?: ")

directory = "/media/andy/1E567E99567E717F/Users/AndyLap/Music/%s/" % channel_name


YTfetcher = YoutubeVideoFetcher(APIkey)
YTdownloader = YoutubeVideoDownloader()
YTconverter = VideoConverter()
YTchannel_downloader = YoutubeChannelDownloader(YTfetcher, YTdownloader, YTconverter)

YTchannel_downloader.download_channel(channel_name, directory)
