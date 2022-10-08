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

def dict_values(d: dict):
    """Get only the values (not keys) from a dictionary"""
    return [v for _, v in d.items()]
