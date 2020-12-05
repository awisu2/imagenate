from typing import List, Any, Tuple
from pathlib import Path
import math

from PIL import Image
from imagenate.libs.enum import CustomEnum

# TODO: 可能ならライブラリのクラス使いたい
class Position:
    x: int = 0
    y: int = 0

    def reset(self):
        self.x = 0
        self.y = 0


class Direction(CustomEnum):
    # 水平
    HORIZONTAL = "horizontal"
    # 垂直
    VERTICAL = "vertical"


def concat_image_by_path(pathes: List[str], **kwargs) -> Image:
    """パスをもとに画像を結合"""

    # パスがファイルであるかチェック
    for path in pathes:
        if not Path(path).is_file():
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


def _get_sizes(grid: List[List[Any]]) -> Tuple[List[int], List[int]]:
    """縦横格子状に並んでいるときの分割サイズを取得

    1行目は3列、２行目は２列などには未対応
    """
    widthes = [0] * len(grid)
    heights = [0] * len(grid[0])

    # 縦横の最大サイズを、行列のサイズとして取得
    for r in range(0, len(grid)):
        line = grid[r]
        for c in range(0, len(line)):
            cel = line[c]
            if heights[r] < cel.height:
                heights[r] = cel.height

            if widthes[c] < cel.width:
                widthes[c] = cel.width

    return widthes, heights


def concat_image(images, *, row: int = 0, col: int = 0) -> Image:
    """画像を結合したオブジェクトを返却"""

    # パラメータチェック
    if not images:
        return None
    if row <= 0 and col <= 0:
        return None

    # TODO: サイズ違いで正方形のグリッドに収まらない場合もある
    # TODO: 詰めて並べる分割
    # TODO: 拡大方法別の分割

    # グリッドに配置
    grid = _get_grids(images, row, col)
    # サイズの取得
    widthes, heights = _get_sizes(grid)
    # 貼り付け
    image = Image.new("RGB", (sum(widthes), sum(heights)))
    pos = Position()
    diff = Position()
    for r in range(0, len(grid)):
        line = grid[r]
        pos.x = 0
        height = heights[r]
        for c in range(0, len(line)):
            cel = line[c]
            width = widthes[c]

            # サイズより小さかった場合、中央になるように調整
            diff.reset()
            if width > cel.width:
                diff.x = (width - cel.width) // 2
            if height > cel.height:
                diff.y = (height - cel.height) // 2

            image.paste(cel, (pos.x + diff.x, pos.y + diff.y))
            pos.x += width
        pos.y += height

    return image
