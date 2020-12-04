from typing import List
from pathlib import Path
from PIL import Image
from enum import Enum


class Direction(Enum):
    # 水平
    HORIZONTAL = "horizontal"
    # 垂直
    VERTICAL = "vertical"


def concat_image_by_path(pathes: List[str], **kwargs) -> Image:
    """パスをもとに画像を結合"""

    # パスがファイルであるかチェック
    for path in pathes:
        if not Path(path):
            print(f"{path} is not file")
            return None

    images: List[Image] = []
    for path in pathes:
        # if not image raise PIL.UnidentifiedImageError
        print(f"== {path}")
        image = Image.open(path)
        images.append(image)

    return concat_image(images, **kwargs)


def concat_image(images, *, direction: Direction = Direction.HORIZONTAL) -> Image:
    """画像を結合したオブジェクトを返却"""
    total_height = 0
    max_height = 0
    total_width = 0
    max_width = 0
    for image in images:
        if max_height < image.height:
            max_height = image.height

        if max_width < image.width:
            max_width = image.width

        total_height += image.height
        total_width += image.width

    # 土台となる画像の作成と貼り付け
    image = None
    if direction == Direction.VERTICAL:
        image = Image.new("RGB", (max_width, total_height))
        y = 0
        for _image in images:
            image.paste(_image, (0, y))
            y += _image.height

    else:
        image = Image.new("RGB", (total_width, max_height))
        x = 0
        for _image in images:
            image.paste(_image, (x, 0))
            x += _image.width

    return image
