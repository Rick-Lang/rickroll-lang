"""
Common/Shared utilities, to use across multiple modules/scripts
"""


from typing import Callable, Final


def starts_ends(container: str | list, x):
    """
    Check if it starts and ends with the same value.

    Examples:
    ```
    starts_ends('"rick"', '"') # `True`
    starts_ends('"rick"', "'") # `False`
    starts_ends('(rick)', '()') # `False`
    ```
    """
    # for some reason, type-inference only works if it explicitly returns a bool
    # WTF?
    return True if container[0] == x and container[-1] == x else False


join_list: Final[Callable[[list], str]] = lambda l: ''.join(map(str, l))
"""Convert any `list` into a `str` without delimiter."""


def remove_all(l: list, x):
    """Remove all occurrences of value (in-place) from a `list` and return it."""
    while x in l:
        l.remove(x)
    return l


filter_str: Final[Callable[[str], str]] = lambda s: s[1:-1]
"""Remove 1st and last chars from a `str`."""


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
