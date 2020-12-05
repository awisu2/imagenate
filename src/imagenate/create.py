from PIL import Image


def create(width: int, height: int, color="#000000"):
    image = Image.new("RGB", (width, height), color=color)
    return image
