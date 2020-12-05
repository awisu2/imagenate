from argparse import ArgumentParser

from imagenate.libs.enum import CustomEnum


class Command(CustomEnum):
    CONCAT = "concat"
    CONCAT_DIR = "concat_dir"
    CREATE = "create"


def create_base_argperser() -> ArgumentParser:
    argparser = ArgumentParser()
    argparser.description = "imgage manager"
    argparser.add_argument("command", type=str, choices=Command.get_values())
    return argparser
