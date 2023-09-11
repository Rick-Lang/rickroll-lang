from typing import Final
from Keywords import *

ALL_KW: Final = "ijustwannatelluhowimfeeling,andifuaskmehowimfeeling,\
give,up,weknowthe,andweregonnaplayit,gonna,gotta,whenigivemy,itwillbecompletely,\
thereaintnomistaking,iftheyevergetudown,takemetourheart,saygoodbye,desertu,\
runaround,togetherforeverandnevertopart,togetherforeverwith,>,<,<=,>=,aint,==,py:"


def lexicalize(stmt: str):

    current_token = ''
    not_in_quote = True
    tokens: list[str] = []

    for char in stmt:

        if char == '"': not_in_quote = not not_in_quote
        if char == '#': break
        if char in {'~', "'"} and not_in_quote:
            continue

        if char in SEPARATORS and not_in_quote:

            if current_token not in {' ', '\n'}:
                # if current_token != '': # this process is moved to order_words()
                tokens.append(current_token)

            if char not in {' ', '\n'}:
                tokens.append(char)

            current_token = ''

        else: current_token += char

    return order_words(tokens)

def order_words(tokens: list[str]):
    """
    token = ['take', 'me', 'to', 'ur', 'heart']
    order_words(token): final token = ['takemetourheart']
    """

    final_token: Final[list[str]] = []
    kw_in_statement = ''
    temp = False

    for tok in tokens:

        if tok in ALL_KW and kw_in_statement + tok in ALL_KW:
            kw_in_statement += tok

        else:
            temp = True

            if kw_in_statement != '':
                final_token.append(kw_in_statement)

            final_token.append(tok)
            kw_in_statement = ''

    if not temp:
        final_token.append(kw_in_statement)

    return final_token
