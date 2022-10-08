from enum import Enum

class KW_ENUM(Enum):
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

    L_OP = 'islessthan'
    G_OP = 'isgreaterthan'
    GOE_OP = 'isgreaterthanorequalto'
    LOE_OP = 'islessthanorequalto'
    IS_NOT_OP = 'aint'
    E_OP = 'is'

    PY = 'py:'

# Keywords
KW_print        = KW_ENUM.PRINT.value
KW_if           = KW_ENUM.IF.value

KW_let          = KW_ENUM.LET.value
KW_assign       = KW_ENUM.ASSIGN.value
KW_import1      = 'weknowthe'
KW_import2      = "andwe'regonnaplayit"
KW_def          = 'gonna'
KW_return1      = 'whenigivemy'
KW_return2      = 'itwillbecompletely'
KW_try          = 'thereaintnomistaking'
KW_except       = 'iftheyevergetudown'
KW_main         = 'takemetourheart'
KW_end          = 'saygoodbye'

KW_break        = 'desertu'
KW_continue     = 'runaround'
KW_endless_loop = 'togetherforeverandnevertopart'
KW_while_loop   = 'togetherforeverwith'

KW_L_OP = 'islessthan'
KW_G_OP = 'isgreaterthan'
KW_GOE_OP = 'isgreaterthanorequalto'
KW_LOE_OP = 'islessthanorequalto'
KW_is_not_OP = 'aint'
KW_E_OP = 'is'

KW_PY = KW_ENUM.PY.value

keywords: list[str] = [e.value for e in KW_ENUM]

INDENT_KW = [KW_ENUM[k].value for k in ['IF', 'DEF', 'TRY', 'EXCEPT', 'WHILE_LOOP', 'ENDLESS_LOOP']]

# Tokens that the interpreter will totally ignore
ignore_tokens = set("~'")

# Characters in numerals
digits = set('0123456789.')

# Separators are used in tokenization
separators = {
    # Don't use `set`, because multi-char `str`s may be added in the future
    '(', ')', '[', ']', '{', '}', ',', '\n', ' ', '+', '-', '*', '/', '%', '^', '='
}

# Operators
operators = {
    '+', '-', '*', '/', '%', '^', '=',
    '[', ']', '(', ')', '{', '}', ',',
    '>', '<', '<=', '>=', '!=', 'is', 'aint'
}
OP_build_in_functions = {'to_string', 'to_int', 'to_float', 'length'}
