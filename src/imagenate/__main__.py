from argparse import ArgumentParser
from imagenate.libs.enum import CustomEnum
from .concat import Direction, concat_image_by_path


class Command(CustomEnum):
    CONCAT = "concat"


def base_argperse() -> ArgumentParser:
    argparser = ArgumentParser()
    argparser.description = "imgage manager"
    argparser.add_argument("command", type=str, choices=Command.get_values())
    return argparser


def main():
    args, _ = base_argperse().parse_known_args()

    if args.command == Command.CONCAT.value:
        concat()


def concat():
    def get_argperser() -> ArgumentParser:
        argperser = base_argperse()
        argperser.add_argument(
            "-d",
            "--direction",
            choices=Direction.get_values(),
            default=Direction.HORIZONTAL,
            help="結合の方向",
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

    image = concat_image_by_path(args.input, direction=args.direction)
    image.save(args.out)


if __name__ == "__main__":
    main()