"""
Common/Shared fns and constants to use across multiple modules/scripts
"""

def join_list(l: list):
    """Convert any `list` into a string without delimiter"""
    return ''.join(map(str, l))

def remove_all(ls: list, __value):
    """Remove all occurrences of value (in-place) and returns the list"""
    while __value in ls:
        ls.remove(__value)
    return ls

def filter_str(s: str):
    """Remove 1st and last chars from a `str`ing"""
    return s[1:-1]

def precedence(op: str):
    """
    Get precedence of basic arithmetic operators (+ - * /).

    `op` should be a char.

    returns `1` for lowest precedence, `2` for highest, `0` if `op` is not recognized
    """
    if op in {'+', '-'}:
        return 1
    if op in {'*', '/'}:
        return 2
    return 0
