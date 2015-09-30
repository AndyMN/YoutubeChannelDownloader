import requests, math

class YoutubeVideoFetcher:

    def __init__(self, APIkey):
        self.apikey = APIkey


    def fetch_videoids(self, channel_name):
        video_ids = []
        playlist_url = "https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername=%s&key=%s" % (channel_name,self.apikey) # First make a request to get the playlist ID of the Uploads Playlist
        req = requests.get(playlist_url)

        playlist_id = req.json()["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"] #This is the ID gotten out of a json response, thanks google
        start_url = "https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId=%s&key=%s" % (playlist_id, self.apikey) #the very first page of the uploads list (50 at a time) this one is seperate because there is no "next page" parameter in this url
        req = requests.get(start_url)

        items = req.json()["items"] #The items in the JSON store the video id's that we need to get the URLs that we download
        for item in items: #Adding all the videoIDs from the items from the first page of results to the videoIds list
            video_ids.append(item["contentDetails"]["videoId"])

        num_items = req.json()["pageInfo"]["totalResults"] #lets see how many items are in the uploads list
        num_items_per_page = 50
        num_pages = int(math.ceil(num_items / num_items_per_page)) #divide the total number by the max amount of requests,50 (hardcoded lolol noob)

        for i in xrange(num_pages):
            try:
                next_page_token = req.json()["nextPageToken"] #get the next page token needed to get the next 50 items in the uploads list
                new_url = "https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&pageToken=%s&playlistId=%s&key=%s" % (next_page_token, playlist_id, self.apikey)
                req = requests.get(new_url)

                items = req.json()["items"] #The items in the JSON store the video id's that we need to get the URLs that we download
                for item in items: #Adding all the videoIDs from the items from the first page of results to the videoIds list
                    video_ids.append(item["contentDetails"]["videoId"])
            except:
                pass

        return video_ids