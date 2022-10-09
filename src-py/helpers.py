"""
Common/Shared fns and constants to use across multiple modules/scripts
"""

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
    return container[0] is x and container[-1] is x

def join_list(l: list):
    """Convert any `list` into a `str` without delimiter."""
    return ''.join(map(str, l))

def remove_all(l: list, x):
    """Remove all occurrences of value (in-place) from a `list` and returns it."""
    while x in l:
        l.remove(x)
    return l

def filter_str(s: str):
    """Remove 1st and last chars from a `str`."""
    return s[1:-1]

def remove_file_ext(f_name: str):
    """
    Return a file-name-path without extension (substring after last dot).

    **WARNING:** if path is a dot-{file/dir} the name (and dot) will be obliterated!

    Examples:
    ```
    remove_file_ext('never_gonna_give_u_up.ogg') # 'never_gonna_give_u_up'

    remove_file_ext('totally not a rickroll.exe') # 'totally not a rickroll'

    remove_file_ext('.rick') # ''
    ```
    """
    return '.'.join(f_name.split('.')[:-1])

def precedence(op: str):
    """
    Get precedence of basic arithmetic operators (+ - * /).

    `op` should be a char.

    returns `1` for lowest precedence, `2` for highest, `0` if `op` is not recognized.
    """
    if op in {'+', '-'}:
        return 1
    if op in {'*', '/'}:
        return 2
    return 0