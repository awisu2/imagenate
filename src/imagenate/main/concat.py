from argparse import ArgumentParser
from pathlib import Path

from imagenate.main.share import create_base_argperser
from imagenate.concat import concat_image_by_path


def get_argperser() -> ArgumentParser:
    argperser = create_base_argperser()
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


def concat():
    """結合処理"""

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
    print(f"saved: {out.absolute()}")
