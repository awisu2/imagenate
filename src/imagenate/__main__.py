from argparse import ArgumentParser
from imagenate.libs.enum import CustomEnum
from .concat import concat_image_by_path


class Command(CustomEnum):
    CONCAT = "concat"


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
        concat()


def concat():
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

    image = concat_image_by_path(args.input, row=args.row, col=args.col)
    if not image:
        print("missing create concat image")
        return

    image.save(args.out)
    print(f"saved {args.out}")


if __name__ == "__main__":
    main()