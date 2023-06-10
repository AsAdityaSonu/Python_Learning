#WAP to automatically download 10 images of cat from “Google Images”. [Hint: Find the package from pypi.org and use it]
import requests
import os

def download_cat_images(num_images):
    url = "https://source.unsplash.com/600x600/?cat"  # URL of the cat image API

    # Create a directory to save the downloaded images
    os.makedirs("cat_images", exist_ok=True)

    for i in range(num_images):
        response = requests.get(url)

        # Generate a unique filename for each image
        file_name = f"cat_images/cat{i+1}.jpg"

        # Save the image to the file
        with open(file_name, "wb") as file:
            file.write(response.content)

        print(f"Downloaded image {i+1} out of {num_images}")

# Call the function and specify the number of images to download (in this case, 10)
download_cat_images(10)
