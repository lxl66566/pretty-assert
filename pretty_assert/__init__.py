import inspect
import sys
from functools import wraps
from types import FrameType

from pprintpp import pformat
from termcolor import colored


def eprintln(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def __get_lines_of_frame_source(frame: FrameType, start: int, end: int):
    """
    Get the lines of source code from a given frame between the specified start and end line numbers.

    Args:
        frame (FrameType): The frame object representing the source code.
        start (int): The starting line number.
        end (int): The ending line number (including).

    Returns:
        list: A list of source code lines between the specified start and end line numbers.
    """
    source_lines, source_start_number = inspect.getsourcelines(frame)
    return source_lines[start - source_start_number - 1 : end - source_start_number]


class GlobalConfig:
    __slots__ = (
        "comment_message_color",
        "other_message_color",
        "code_color",
        "line_number_color",
        "exit",
    )

    def __init__(self, **kwargs):
        self.set(**kwargs)

    def set(self, **kwargs):
        kwargs.setdefault("comment_message_color", "red")
        kwargs.setdefault("other_message_color", "white")
        kwargs.setdefault("code_color", "yellow")
        kwargs.setdefault("line_number_color", "grey")
        kwargs.setdefault("exit", True)
        for k, v in kwargs.items():
            setattr(self, k, v)
        return self


global_config = None


def init(**kwargs):
    global global_config
    global_config = GlobalConfig(**kwargs)

    return global_config


def _get_or_init(**kwargs):
    global global_config
    if global_config is None:
        global_config = GlobalConfig(**kwargs)


def pretty_wrapper(func, *args):
    @wraps(func)
    def wrapper(*args):
        _get_or_init()

        args_len = len(inspect.getfullargspec(func).args)
        result: bool = func(*args[:args_len])
        comment = args[-1] if len(args) > args_len else None
        if result:
            return True

        frame = inspect.currentframe().f_back
        filename = inspect.getfile(frame)
        frame_stack = inspect.stack()[1]
        start = frame_stack.positions.lineno
        end = frame_stack.positions.end_lineno
        source_code = __get_lines_of_frame_source(frame, start, end)

        eprintln(f"Assertion Error in `{filename}`, line {start}:")
        for line_index, line in enumerate(source_code):
            eprintln(
                colored(line_index + start, global_config.line_number_color),
                "  ",
                colored(line.rstrip(), global_config.code_color),
                sep="",
            )

        if comment is not None:
            eprintln(
                f"Comment: {colored(comment, global_config.comment_message_color)}"
            )
        sys.exit(1)

    return wrapper


@pretty_wrapper
def assert_eq(a, b):
    result = a == b
    if result:
        return True
    str_a = pformat(a)
    str_b = pformat(b)
    eprintln(f"Not equal: {colored(str_a, 'red')} != {colored(str_b, 'green')}")
    return False


assert_eq(1, 1)
assert_eq(
    1,
    2,
    "message",
)
