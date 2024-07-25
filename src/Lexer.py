from typing import Final

ALL_KW: Final = "ijustwannatelluhowimfeeling,andifuaskmehowimfeeling,\
give,up,weknowthe,andweregonnaplayit,gonna,gotta,whenigivemy,itwillbecompletely,\
thereaintnomistaking,iftheyevergetudown,takemetourheart,saygoodbye,desertu,\
runaround,togetherforeverandnevertopart,togetherforeverwith,>,<,<=,>=,aint,==,py:"

SEPARATORS: Final = {
    '(', ')', '[', ']', '{', '}', ',', '\n', ' ', '+', '-', '*', '/', '%', '^', '='
}

import re

token_specification = [
    ('NUMBER',    r'\d+(\.\d*)?'),                  # Integer or decimal number
    ('ASSIGN',    r'='),                            # Assignment operator
    ('ID',        r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),   # Identifiers
    ('OP',        r'[+\-*/%><()[\]]'),              # Arithmetic operators
    ('SEP',       r'[,.]'),
    ('COMMENT',   r'#(.*)'),                        # Comment
    ('STR',       r'"([^"]*)"'),                    # String
    ('NEWLINE',   r'\n'),                           # Line endings
    ('SKIP',      r'[ \t]+'),                       # Skip over spaces and tabs
    ('MISMATCH',  r'.'),                            # Any other character
]

token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

# The tokenizer function
def tokenize(code: str) -> list[tuple[str, str]]:
    """
    Tokenizes the given string of code into a list of tokens.

    Args:
        code (str): The code to be tokenized.

    Returns:
        list[tuple[str, str]]: A list of tokens defined as tuple(KIND, VALUE) extracted from the statement.
    """
    tokens = []

    lineno = 1
    line_start = 0
    previous_token = ('', '')
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()

        if kind == 'ID':
            if (previous_token[0] == 'ID' or previous_token[0] == 'KW')\
                and previous_token[1] + value in ALL_KW:
                previous_token = ('KW', previous_token[1] + value)
                tokens[-1] = previous_token
                continue

        elif kind == 'SKIP':
            continue
        elif kind == 'COMMENT':
            continue
        elif kind == 'NEWLINE':
            lineno += 1
            line_start = mo.end()
            continue
        

        previous_token = (kind, value)
        tokens.append(previous_token)

    return tokens



