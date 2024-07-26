from typing import Final

ALL_KW: Final = "ijustwannatelluhowimfeeling,andifuaskmehowimfeeling,\
give,up,weknowthe,andweregonnaplayit,gonna,gotta,whenigivemy,itwillbecompletely,\
thereaintnomistaking,iftheyevergetudown,takemetourheart,saygoodbye,desertu,\
runaround,togetherforeverandnevertopart,togetherforeverwith,>,<,<=,>=,aint,==,py:"

SEPARATORS: Final = {
    '(', ')', '[', ']', '{', '}', ',', '\n', ' ', '+', '-', '*', '/', '%', '^', '='
}

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
