from typing import List, Any
from pathlib import Path
import math

from PIL import Image
from imagenate.libs.enum import CustomEnum


class Direction(CustomEnum):
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
        image = Image.open(path)
        images.append(image)

    return concat_image(images, **kwargs)


def _get_grids(images, row: int, col: int) -> List[List[Any]]:
    grid = []

    r = 0
    c = 0
    line = []

    # colが無限(=0)で、rowが指定されている場合等分して配置
    if row > 0 and col == 0:
        col = math.floor(len(images) / row)

    for image in images:
        line.append(image)
        c += 1

        if col <= c:
            grid.append(line)
            r += 1
            c = 0
            line = []
            if row <= r:
                break

    if line:
        grid.append(line)

    # TODO: ループして埋まるで配置？
    return grid


def concat_image(images, *, row: int = 0, col: int = 0) -> Image:
    """画像を結合したオブジェクトを返却"""

    # パラメータチェック
    if not images:
        return None
    if row <= 0 and col <= 0:
        return None

    # グリッドに配置
    # TODO: サイズ違いで正方形のグリッドに収まらない場合もある
    grid = _get_grids(images, row, col)

    # 最終的なサイズなどを取得
    # TODO: 詰めて並べる分割
    # TODO: 拡大方法別の分割

    # 等分のサイズでの分割
    height = 0
    width = 0
    for line in grid:
        # 行の情報を収集
        line_width = 0
        line_height = 0
        size_line = []
        for cel in line:
            size_cel = (cel.width, cel.height)
            size_line.append(size_cel)

            line_width += cel.width
            if line_height < cel.height:
                line_height = cel.height

        # 土台用に調整
        height += line_height

        if width < line_width:
            width = line_width

    # 土台となる画像の作成と貼り付け
    image = Image.new("RGB", (width, height))
    x = 0
    y = 0
    for line in grid:
        x = 0
        max_height = 0
        for cel in line:
            image.paste(cel, (x, y))
            x += cel.width
            if cel.height > max_height:
                max_height = cel.height
        y += max_height

    return image
