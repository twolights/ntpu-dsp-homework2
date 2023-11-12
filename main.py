import sys
from typing import Tuple

from system import H_of_omega
import figures

COMMAND_SHOW = 'show'
COMMAND_GENERATE = 'gen'
AVAILABLE_COMMANDS = COMMAND_SHOW, COMMAND_GENERATE


def parse_command(args) -> Tuple[str, str]:
    if len(args) == 0:
        return COMMAND_GENERATE, figures.ALL
    command = args[0]
    if command not in AVAILABLE_COMMANDS:
        raise RuntimeError(f"Unrecognized command f{command}")
    if len(args) == 1:
        what = figures.ALL
    else:
        what = args[1]
    if not what == figures.ALL and what not in figures.AVAILABLE_FIGURES:
        raise RuntimeError(f"Unrecognized figure {what}")
    return command, what


def main() -> None:
    command, what = parse_command(sys.argv[1:])
    if what == figures.ALL:
        fig_ids = figures.AVAILABLE_FIGURES
    else:
        fig_ids = tuple(what)
    for fig_id in fig_ids:
        figure = figures.get_figure(fig_id, H_of_omega)
        if command == COMMAND_SHOW:
            figure.show()
        elif command == COMMAND_GENERATE:
            filename = f"{fig_id}.png"
            figure.save(filename=filename)


if __name__ == '__main__':
    main()
