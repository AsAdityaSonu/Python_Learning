#WAP to automatically download 10 images of cat from “Google Images”. [Hint: Find the package from pypi.org and use it]
#<------------Not Downloading------------>
from google_images_download import google_images_download

def download_images(keyword, limit):
    response = google_images_download.googleimagesdownload()
    arguments = {
        "keywords": keyword,
        "limit": limit,
        "print_urls": True,
        "output_directory": "cat_images",
    }
    paths = response.download(arguments)
    return paths[keyword]

download_images("cat",10)