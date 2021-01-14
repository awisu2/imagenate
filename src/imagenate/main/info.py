from argparse import ArgumentParser
from pathlib import Path

from .share import create_base_argperser
from imagenate.info import get_info


def create_argperser() -> ArgumentParser:
    argperser = create_base_argperser()
    argperser.add_argument(
        "image",
        help="画像パス",
    )
    return argperser


def info():
    args = create_argperser().parse_args()

    # パラメータチェック

    # 画像作成
    image = Path(args.image)
    if not image.is_file():
        print(f'"{image}" is not file')
        return

    info = get_info(image)
    print(info)
