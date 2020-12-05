from .main.share import create_base_argperser, Command
from .main.create import create
from .main.concat import concat, concat_dir


def main():
    """コマンド呼び出し"""
    args, _ = create_base_argperser().parse_known_args()
    command = Command(args.command)

    if command == Command.CONCAT:
        concat()
    if command == Command.CONCAT_DIR:
        concat_dir()
    elif command == Command.CREATE:
        create()


if __name__ == "__main__":
    main()