import requests

def download_image(url, save_path):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve image. Error: {e}")

# Example usage
print("Hello world")
image_url = "https://cf.shopee.vn/file/bbd4c7d2dd879e188410b9bf944de5c5"
save_path = "downloaded_image.jpg"
download_image(image_url, save_path)
print("Goodbye world")