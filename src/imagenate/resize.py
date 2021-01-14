from imagenate.libs.enum import CustomEnum

from PIL import Image


class ResizeKind(CustomEnum):
    """結合処理時の各セルの中で位置調整"""

    INNER = "inner"
    FORCE = "force"
    OUTER = "outer"

    @classmethod
    def get_help(cls):
        helps = []
        for item in list(cls):
            help = ""
            if item == cls.INNER:
                help = "内側に合わせる(縦横比:継承,サイズ:小さい可能性)"
            elif item == cls.FORCE:
                help = "指定サイズ通り(縦横比:変化,サイズ:指定通り)"
            if item == cls.OUTER:
                help = "はみ出して合わせる(縦横比:継承,サイズ:指定通り)"

            helps.append("{}: {}".format(item.value, help))

        return ", ".join(helps)


def get_rate_for_resize(
    image: Image, width: int, height: int, *, kind: ResizeKind = ResizeKind.INNER
):
    rate = 1
    if image.width == width and image.height == height:
        return rate

    # 比率的に画像の横幅のほうが大きいまたは同じ
    aspect_ratios = [image.width / image.height, width / height]
    is_over_width = aspect_ratios[0] >= aspect_ratios[1]

    # 変換後のサイズ取得
    if kind == ResizeKind.INNER:
        if is_over_width:
            rate = width / image.width
        else:
            rate = height / image.height
    elif kind == ResizeKind.OUTER:
        if is_over_width:
            rate = height / image.height
        else:
            rate = width / image.width

    return rate


def resize(
    image: Image, width: int, height: int, *, kind: ResizeKind = ResizeKind.INNER
):
    if width == 0:
        width = image.width
    if height == 0:
        height = image.height

    if kind == ResizeKind.FORCE:
        return image.resize((width, height), resample=Image.NEAREST)

    rate = get_rate_for_resize(image, width, height, kind=kind)
    if not rate == 1:
        image = image.resize((int(image.width * rate), int(image.height * rate)))

    # 指定サイズを超えている場合は切り抜き(OUTERのとき発生する可能性)
    if image.width >= width and image.height >= height:
        left = (image.width - width) // 2
        upper = (image.height - height) // 2
        box = (
            left,
            upper,
            left + width,
            upper + height,
        )
        image = image.crop(box)

    return image
