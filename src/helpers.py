"""
Common/Shared utilities, to use across multiple modules/scripts
"""


from typing import Callable, Final

def starts_ends(s: str, char: str):
    """
    Check if it starts and ends with the same char.

    Examples:
    ```
    starts_ends('"rick"', '"') # `True`
    starts_ends('"rick"', "'") # `False`
    starts_ends('(rick)', '()') # `False`
    ```
    """

    return True if s[0] == char and s[-1] == char else False


join_list: Final[Callable[[list], str]] = lambda l: ''.join(l)
"""Convert any `list` into a `str` without delimiter."""


def remove_all(l: list, x):
    """Remove all occurrences of value (in-place) from a `list` and return it."""
    while x in l:
        l.remove(x)
    return l

def filter_str(s:str):
    """
    Remove 1st and last chars, and
    replace line-feed literals with actual line-feeds.
    """
    return s[1:-1].replace("\\n", "\n")

def precedence(op: str):
    """
    Get precedence of basic arithmetic operators (+ - * /).

    `op` should be a char.

    returns `1` for lowest precedence, `2` for highest, `0` if `op` is not recognized.
    """
    if op in ('+', '-'):  # tiny `tuple`s are faster than tiny `list`s and `set`s
        return 1
    if op in ('*', '/'):
        return 2
    return 0
