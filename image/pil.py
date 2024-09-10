from PIL import Image
import base64
from io import BytesIO

# pip install pillow
# https://pillow.readthedocs.io/en/stable/


def imgShow(file):
    """use the default system application the open the image"""
    try:
        image = Image.open(file)
        image.show()
    except OSError as e:
        print(f"Error opening file: {e}")


def imgInfo(file):
    """get a dict with information about the image"""
    try:
        image = Image.open(file)
        width, height = image.size
        return({'width': width, 'height': height})
    except OSError as e:
        print(f"Error opening file: {e}")


def imgResize(file, new_file, width, height):
    """resize the image."""
    try:
        image = Image.open(file)
        resized_image = image.resize((width, height))  # Resize to 256x256 pixels
        resized_image.save(new_file)
    except OSError as e:
        print(f"Error resizing file: {e}")

def imgGrey(file, new_file):
    """creates a new greyscale version of the file."""
    try:
        image = Image.open(file)
        grey_image = image.convert("L")  # Resize to 256x256 pixels
        grey_image.save(new_file)
    except OSError as e:
        print(f"Error greyscale the file: {e}")

def imgThumb(file, new_file, size):
    """Creates a thumbnail of the image at the specified path and saves it.
    """
    try:
        image = Image.open(file)
        image.thumbnail((size, size))  # Resize image with aspect ratio preserved
        image.save(new_file)
    except OSError as e:
        print(f"Error creating thumbnail: {e}")

def convert_to_base64(file_path):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """

    pil_image = Image.open(file_path)
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str
