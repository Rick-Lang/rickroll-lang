from typing import Final
from enum import Enum


class KW(Enum):
    """Keywords"""
    PRINT = 'ijustwannatelluhowimfeeling'
    IF = 'andifuaskmehowimfeeling'

    LET = 'give'
    ASSIGN = 'up'
    IMPORT1 = 'weknowthe'
    IMPORT2 = "andwe'regonnaplayit"
    DEF = 'gonna'
    RETURN1 = 'whenigivemy'
    RETURN2 = 'itwillbecompletely'
    TRY = 'thereaintnomistaking'
    EXCEPT = 'iftheyevergetudown'
    MAIN = 'takemetourheart'
    END = 'saygoodbye'

    BREAK = 'desertu'
    CONTINUE = 'runaround'
    ENDLESS_LOOP = 'togetherforeverandnevertopart'
    WHILE_LOOP = 'togetherforeverwith'

    G_OP = 'isgreaterthan'
    L_OP = 'islessthan'
    GOE_OP = 'isgreaterthanorequalto'
    LOE_OP = 'islessthanorequalto'
    IS_NOT_OP = 'aint'
    E_OP = 'is'

    PY = 'py:'


KEYWORDS: Final[list[str]] = [e.value for e in KW]
"""values in `KW`"""

INDENT_KW: Final = [KW[k].value for k in ['IF', 'DEF', 'TRY', 'EXCEPT', 'WHILE_LOOP', 'ENDLESS_LOOP']]
"""keywords that require indentation in their body (when transpiled to py)"""

IGNORE_TOKENS: Final = set("~'")
"""Tokens that the interpreter will totally ignore"""

DIGITS: Final = set('0123456789.')
"""Characters in numerals"""

SEPARATORS: Final = {
    # not using `set`, because readability, and multi-char `str`s may be added in the future
    '(', ')', '[', ']', '{', '}', ',', '\n', ' ', '+', '-', '*', '/', '%', '^', '='
}
"""Separators are used in tokenization"""

OPERATORS: Final = {
    '+', '-', '*', '/', '%', '^', '=', '&', '|',
    '[', ']', '(', ')', '{', '}', ',',
    '>', '<', '<=', '>=', '!=', 'is', 'aint'
}
OP_BUILT_IN_FUNCTIONS: Final = {'to_string', 'to_int', 'to_float', 'length'}
