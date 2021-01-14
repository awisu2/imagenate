from argparse import ArgumentParser
from pathlib import Path

from .share import create_base_argperser
from imagenate.resize import resize as _resize

from PIL import Image


def create_argperser() -> ArgumentParser:
    argperser = create_base_argperser()
    argperser.add_argument(
        "-w",
        "--width",
        type=int,
        required=False,
        default=0,
        help="画像の幅",
    )
    argperser.add_argument(
        "--height",
        type=int,
        required=False,
        default=0,
        help="画像の高さ",
    )
    argperser.add_argument(
        "-o",
        "--out",
        type=str,
        required=False,
        default="",
        help="出力先",
    )
    argperser.add_argument(
        "image",
        help="画像パス",
    )
    return argperser


def resize():
    args = create_argperser().parse_args()

    # パラメータチェック
    image = args.image
    width = args.width or 0
    height = args.height or 0
    out = args.out or image

    imagePath = Path(image)
    if not imagePath.is_file():
        print(f'"{imagePath}" is not file')
        return
    _image = Image.open(imagePath)

    # リサイズ
    image = _resize(_image, width, height)
    image.save(Path(out))
