from argparse import ArgumentParser
from pathlib import Path

from imagenate.main.share import create_base_argperser
from imagenate.concat import concat_image_by_path, concat_image_by_dir, CelPosition


def _get_argperser() -> ArgumentParser:
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
        "--cel_position",
        type=str,
        choices=CelPosition.get_values(),
        default=CelPosition.CENTER,
        help="結合時に余白が出た際の位置調整",
    )
    return argperser


def get_concat_argperser() -> ArgumentParser:
    argperser = _get_argperser()
    argperser.add_argument(
        "-i",
        "--input",
        nargs="*",
        type=str,
        required=True,
        help="結合対象の画像パスリスト",
    )
    argperser.add_argument(
        "-o",
        "--out",
        required=True,
        help="出力先の画像パス",
    )
    return argperser


def get_concat_dir_argperser() -> ArgumentParser:
    argperser = _get_argperser()
    argperser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help="結合対象の画像が存在するディレクトリ",
    )
    argperser.add_argument(
        "-o",
        "--out",
        type=str,
        help='出力先ディレクトリ。変換ディレクトリに内に "concat_{yymmddhhmmss}" ディレクトリを作成し出力',
    )
    argperser.add_argument(
        "--prefix",
        type=str,
        default="concat",
        help="結合ファイル名のprefix (default=concat)",
    )
    argperser.add_argument(
        "--ext",
        type=str,
        default=".png",
        help="出力ファイル拡張子",
    )
    argperser.add_argument(
        "--add_dir",
        action="store_true",
        help="出力先にinputと同名のディレクトリを追加する",
    )
    argperser.add_argument(
        "--add_verbose",
        action="store_true",
        help="分割数などを出力ディレクトリに追加する(例: c=3, r=2のとき _3x2が追加される)",
    )
    return argperser


def concat():
    """結合処理"""

    # パラメータチェック
    args = get_concat_argperser().parse_args()
    if args.row <= 0 and args.col <= 0:
        print("row or col must have a value greater than or equal to 0")
        return

    # 処理
    out = Path(args.out)
    cel_position = CelPosition(args.cel_position)
    image = concat_image_by_path(
        args.input, row=args.row, col=args.col, cel_position=cel_position
    )
    if not image:
        print("missing create concat image")
        return

    image.save(out)
    print(f"saved: {out.absolute()}")


def concat_dir():
    """結合処理 ディレクトリ"""

    # パラメータチェック
    args = get_concat_dir_argperser().parse_args()
    if args.row <= 0 or args.col <= 0:
        print("row and col must have a value greater than or equal to 0")
        return

    # 処理
    cel_position = CelPosition(args.cel_position)
    created_pathes = concat_image_by_dir(
        args.input,
        args.out,
        args.row,
        args.col,
        cel_position=cel_position,
        prefix=args.prefix,
        ext=args.ext,
        add_dir=args.add_dir,
        add_verbose=args.add_verbose,
    )

    print("created:")
    for path in created_pathes:
        print(path.absolute())
