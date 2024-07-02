import requests
from PIL import Image
from io import BytesIO

def open_image_from_url(image_url):
    try:
        # Download the image
        response = requests.get(image_url)
        response.raise_for_status()

        # Open the image using Pillow
        image = Image.open(BytesIO(response.content))

        # Display the image
        image.show()

    except Exception as e:
        print(f"Error: {e}")

# Example usage
image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-FdusmMTmGgCjuSDuMMYyZn1t/user-JWKSJ95iQ5j5orR5LOZKbIZA/img-OVDe5fbVDRS4X7RS4NhZZ9TZ.png?st=2023-12-08T23%3A52%3A28Z&se=2023-12-09T01%3A52%3A28Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-12-08T23%3A13%3A12Z&ske=2023-12-09T23%3A13%3A12Z&sks=b&skv=2021-08-06&sig=dXKtXNHVphVJwckh%2Br%2BT9KU7gTAo8JK4tyJPUcNGXOs%3D"
open_image_from_url(image_url)
