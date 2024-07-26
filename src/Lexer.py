from typing import Final

ALL_KW: Final = "ijustwannatelluhowimfeeling,andifuaskmehowimfeeling,\
give,up,weknowthe,andweregonnaplayit,gonna,gotta,whenigivemy,itwillbecompletely,\
thereaintnomistaking,iftheyevergetudown,takemetourheart,saygoodbye,desertu,\
runaround,togetherforeverandnevertopart,togetherforeverwith,>,<,<=,>=,aint,==,py:"

SEPARATORS: Final = {
    '(', ')', '[', ']', '{', '}', ',', '\n', ' ', '+', '-', '*', '/', '%', '^', '='
}

# def tokenize(code: str) -> list[tuple[str, str]]:
#     """
#     Tokenizes the given string of code into a list of tokens.

#     Args:
#         code (str): The code to be tokenized.

#     Returns:
#         list[tuple[str, str]]: A list of tokens defined as tuple(KIND, VALUE) extracted from the statement.
#     """
#     tokens = []

#     lineno = 1
#     line_start = 0
#     previous_token = ('', '')
#     for mo in re.finditer(token_regex, code):
#         kind = mo.lastgroup
#         value = mo.group()

#         if kind == 'ID':
#             if (previous_token[0] == 'ID' or previous_token[0] == 'KW')\
#                 and previous_token[1] + value in ALL_KW:
#                 previous_token = ('KW', previous_token[1] + value)
#                 tokens[-1] = previous_token
#                 continue

#         elif kind == 'SKIP':
#             continue
#         elif kind == 'COMMENT':
#             continue
#         elif kind == 'NEWLINE':
#             lineno += 1
#             line_start = mo.end()
#             continue
        

#         previous_token = (kind, value)
#         tokens.append(previous_token)

#     return tokens


def tokenize(code: str) -> list[tuple[str, str]]:
    """
    Tokenizes the given string of code into a list of tokens.

    Args:
        code (str): The code to be tokenized.

    Returns:
        list[tuple[str, str]]: A list of tokens defined as tuple(KIND, VALUE) extracted from the statement.
    """
    tokens = []

    current_token = ''
    previous_token = ''
    lineno = 1
    in_quote = False

    for c in code:
        if c == '"':
            in_quote = not in_quote

        if in_quote:
            current_token += c
            continue

        if c == '#':
            # Comment encountered, ignore the rest of the line
            break
        elif c in SEPARATORS:
            if current_token.strip():

                # if previous token is a possible identifier
                if previous_token and previous_token + current_token in ALL_KW:
                    previous_token += current_token
                    tokens[-1] = previous_token
                    current_token = ''

                else:
                    tokens.append(current_token)
                    current_token = ''
                    previous_token = tokens[-1]

            if c.strip():
                tokens.append(c)

        else:
            current_token += c

    return tokens