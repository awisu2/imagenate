from pathlib import Path
from PIL import Image


def concat_image_by_path(path1:str, path2:str) -> Image:
    """パスをもとに画像を結合
    """
    if not Path(path1).is_file() or not Path(path2).is_file():
        return None

    # if not image raise PIL.UnidentifiedImageError
    img1 = Image.open(path1)
    img2 = Image.open(path2)

    return concat_image(img1, img2)

# 
def concat_image(img1:Image, img2:Image) -> Image:
    """画像を結合したオブジェクトを返却
    """
    height = img1.height if img1.height > img2.height else img2.height
    img = Image.new('RGB',(img1.width + img2.width,  height))

    img.paste(img1, (0,0))
    img.paste(img2, (img1.width,0))
    return img
