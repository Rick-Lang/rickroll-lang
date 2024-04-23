from typing import Final
from Keywords import *

ALL_KW: Final = "ijustwannatelluhowimfeeling,andifuaskmehowimfeeling,\
give,up,weknowthe,andweregonnaplayit,gonna,gotta,whenigivemy,itwillbecompletely,\
thereaintnomistaking,iftheyevergetudown,takemetourheart,saygoodbye,desertu,\
runaround,togetherforeverandnevertopart,togetherforeverwith,>,<,<=,>=,aint,==,py:"


def lexicalize(stmt: str) -> list[str]:
    """
    Tokenizes the given statement into a list of tokens.

    Args:
        stmt (str): The statement to be tokenized.

    Returns:
        list[str]: A list of tokens extracted from the statement.
    """
    tokens: list[str] = []
    current_token = ""
    in_quote = False

    for char in stmt:
        if char == '"':
            in_quote = not in_quote

        if not in_quote:
            if char == '#':
                # Comment encountered, ignore the rest of the line
                break
            elif char in {'~', "'"}:
                # Ignore tilde and single quote characters
                continue
            elif char in SEPARATORS:
                if current_token.strip():
                    tokens.append(current_token.strip())
                    current_token = ""
                if char.strip():
                    tokens.append(char.strip())
            else:
                current_token += char
        else:
            current_token += char

    if current_token.strip():
        tokens.append(current_token.strip())

    return order_words(tokens)


def order_words(tokens: list[str]) -> list[str]:
    """
    Orders the tokens by combining consecutive tokens that form a keyword.

    Args:
        tokens (list[str]): A list of tokens.

    Returns:
        list[str]: A list of tokens with combined keywords.
    """
    final_tokens: list[str] = []
    kw_buffer = ""

    for token in tokens:
        if token in ALL_KW and kw_buffer + token in ALL_KW:
            # Combine consecutive tokens that form a keyword
            kw_buffer += token
        else:
            if kw_buffer:
                final_tokens.append(kw_buffer)
                kw_buffer = ""
            final_tokens.append(token)

    if kw_buffer:
        final_tokens.append(kw_buffer)

    return final_tokens
