from argparse import ArgumentParser
from pathlib import Path

from PIL import Image

from imagenate.libs.enum import CustomEnum
from .concat import concat_image_by_path


class Command(CustomEnum):
    CONCAT = "concat"
    CREATE = "create"


def base_argperse() -> ArgumentParser:
    argparser = ArgumentParser()
    argparser.description = "imgage manager"
    argparser.add_argument("command", type=str, choices=Command.get_values())
    return argparser


def main():
    """コマンド呼び出し"""
    args, _ = base_argperse().parse_known_args()
    command = Command(args.command)

    if command == Command.CONCAT:
        _concat()
    elif command == Command.CREATE:
        _create()


def _concat():
    """結合処理"""

    def get_argperser() -> ArgumentParser:
        argperser = base_argperse()
        argperser.add_argument(
            "-r",
            "--row",
            type=int,
            default=0,
            help="縦の行数(default=0, 0の場合は無限)",
        )
        argperser.add_argument(
            "-c",
            "--col",
            type=int,
            default=0,
            help="横の行数(default=0, 0の場合は無限)",
        )
        argperser.add_argument(
            "-i",
            "--input",
            nargs="*",
            type=str,
            required=True,
            help="結合対象の画像リスト",
        )
        argperser.add_argument(
            "-o",
            "--out",
            required=True,
            help="出力先の画像パス",
        )
        return argperser

    args = get_argperser().parse_args()

    # パラメータチェック
    if args.row <= 0 and args.col <= 0:
        print("row or col must have a value greater than or equal to 0")
        return

    # 処理
    out = Path(args.out)
    image = concat_image_by_path(args.input, row=args.row, col=args.col)
    if not image:
        print("missing create concat image")
        return

    image.save(out)
    print(f"saved: {out.absolute}")


def _create():
    def get_argperser() -> ArgumentParser:
        argperser = base_argperse()
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

    args = get_argperser().parse_args()

    # パラメータチェック

    # 画像作成
    out = Path(args.out)
    image = Image.new("RGB", (args.width, args.height), color=args.color)
    image.save(out)

    print(f"saved: {out.absolute()}")


if __name__ == "__main__":
    main()