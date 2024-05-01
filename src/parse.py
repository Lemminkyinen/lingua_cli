from pathlib import Path

from models import BaseWord


def read_words(file: str) -> list[BaseWord]:
    with Path(file).open() as f:
        lines = f.read().splitlines()

    return [BaseWord.parse_from_line(line) for line in lines]
