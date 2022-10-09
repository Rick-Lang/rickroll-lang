from Keywords import *
from helpers import remove_all

ALL_KW_STR = ','.join(keywords)

def lexicalize(stmt: str):
    current_token = ''
    quote_count = 0
    tokens: list[str] = []
    for char in stmt:
        if char == '"': quote_count += 1
        if char == '#': break
        if char in ignore_tokens and quote_count % 2 == 0:
            continue

        if char in separators and quote_count % 2 == 0:
            if current_token not in {' ', '\n'}:
                tokens.append(current_token)
            if char not in {' ', '\n'}:
                tokens.append(char)

            current_token = ''
        else: current_token += char

    return order_words(tokens)

def order_words(tokens: list[str]):
    """
    if current `token+kw_in_statement` is in all keyword string, `kw_in_statement += token`
    if current `token+kw_in_statement` not in all keyword string, add `kw_in_statement` to `final_token`
    if statement is ended, add `kw_in_statement` to `final_token`
    """
    final_token: list[str] = []
    kw_in_statement = ''
    temp = False
    for tok in tokens:
        if tok in ALL_KW_STR and kw_in_statement + tok in ALL_KW_STR:
            kw_in_statement += tok

        else:
            temp = True
            final_token.append(kw_in_statement)
            kw_in_statement = ''
            final_token.append(tok)

    if not temp:
        final_token.append(kw_in_statement)

    return remove_all(final_token, '')
