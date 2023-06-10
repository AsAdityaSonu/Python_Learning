#WAP to automatically download 10 videos of “Machine Learning” from “Youtube.com”. [Hint: Find the package from pypi.org and use it]
#<------------Not Downloading------------>
from youtubesearchpython import VideosSearch
from pytube import YouTube

# Search query for YouTube videos
search_query = "Machine Learning"

# Number of videos to download
num_videos = 10

# Perform YouTube search
videos_search = VideosSearch(search_query, limit=num_videos)

# Download function
def download_video(url):
    try:
        # Create a YouTube object
        youtube = YouTube(url)

        # Get the best available video stream
        video_stream = youtube.streams.get_highest_resolution()

        # Download the video
        video_stream.download(output_path='path/to/save/videos')

        print(f"Downloaded: {youtube.title}")

    except Exception as e:
        print(f"Error downloading video: {url}")
        print(str(e))

# Download videos from search results
for video in videos_search.result()["result"]:
    video_url = "https://www.youtube.com/watch?v=" + video['id']
    download_video(video_url)
