import os
from pytube import YouTube

def download_videos(keyword, limit, output_directory):
    query = keyword + " videos"
    search_url = f"https://www.youtube.com/results?search_query={query}&sp=EgIQAQ%253D%253D"
    videos = YouTube.search(url=search_url, max_results=limit)
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Download the videos
    for video in videos:
        try:
            yt = YouTube(video)
            stream = yt.streams.get_highest_resolution()
            filename = stream.default_filename
            output_path = os.path.join(output_directory, filename)
            print(f"Downloading: {filename}")
            stream.download(output_path)
        except Exception as e:
            print(f"Error downloading video: {e}")

# Set the keyword (e.g., "Machine Learning"), the number of videos to download, and the output directory
keyword = "Machine Learning"
limit = 10
output_directory = "./videos"  # Change this path to your desired folder location

# Download the videos
download_videos(keyword, limit, output_directory)