from argparse import ArgumentParser
from pathlib import Path

from PIL import Image

from .share import create_base_argperser


def create_argperser() -> ArgumentParser:
    argperser = create_base_argperser()
    argperser.add_argument(
        "-w",
        "--width",
        type=int,
        required=True,
        help="画像の幅",
    )
    argperser.add_argument(
        "--height",
        type=int,
        required=True,
        help="画像の高さ",
    )
    argperser.add_argument(
        "-o",
        "--out",
        required=True,
        help="出力先の画像パス",
    )
    argperser.add_argument(
        "-c",
        "--color",
        default="#000000",
        help="画像色",
    )
    return argperser


def create():
    args = create_argperser().parse_args()

    # パラメータチェック

    # 画像作成
    out = Path(args.out)
    image = Image.new("RGB", (args.width, args.height), color=args.color)
    image.save(out)

    print(f"saved: {out.absolute()}")
