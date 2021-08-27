from sys import stdout
from random import choice

# Keywords

KW_print        = 'ijustwannatelluhowimfeeling'
KW_if           = 'andifuaskmehowimfeeling'

KW_let          = 'give'
KW_assign       = 'up'
KW_import1      = 'weknowthe'
KW_import2      = "andwe'regonnaplayit"
KW_def1         = 'neverknew'
KW_def2         = 'couldfeelthisway'
KW_return1      = 'whenigivemy'
KW_return2      = 'itwillbecompletely'
KW_main         = 'takemetourheart'
KW_end          = 'saygoodbye'

KW_break        = 'desertu'
KW_continue     = 'runaround'
KW_endless_loop = 'togetherforeverandnevertopart'
KW_while_loop   = 'togetherforeverwith'

keywords = [
    KW_print,
    KW_if,
    KW_let,
    KW_assign,
    KW_import1,
    KW_import2,
    KW_def1,
    KW_def2,
    KW_return1,
    KW_return2,
    KW_main,
    KW_end,
    KW_break,
    KW_continue,
    KW_endless_loop,
    KW_while_loop
]

all_keyword_string = ''
for i in keywords:
    all_keyword_string += i

# Tokens that the interpreter will totally ignore
ignore_tokens = {'~', "'"}

# Characters in numbers
digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}

# Separators are used in tokenization
separators = {
    '(', ')', '[', ']', '{', '}', ',', '\n', ' ', '+', '-', '*', '/', '%', '^', '='
}

# Operators
OP_arithmetic = {'+', '-', '*', '/', '%', '^'}
OP_relational = {'is', 'is_not', 'is_greater_than', 'is_less_than', 'and', 'or'}
OP_assignment = {'='}
OP_other      = {'[', ']', '(', ')', '{', '}', ','}

OP_build_in_functions = {'to_string', 'to_int', 'to_float', 'length'}

error_lyrics = [
    '"If you knew what Im feeling, you would not say no~"',
    '"You know the rules, and so do I~"',
    '"'+"There ain't no mistaking, is true love we are making~"+'"'
]

def join_list(l):
    result = ''
    for i in l: result += f'{i}'
    return result


def error(error_msg):
    stdout.write(error_msg)
    exit('------'*10 + '\n' + choice(error_lyrics))
