from PublicVariables import *

all_keyword_string = ''.join(keywords)


def lexicalize(stmt):
    return order_tokens(tokens=basic_tokenize(stmt))


def basic_tokenize(stmt):
    current_token = ''
    quote_count = 0
    tokens = []
    for char in stmt:

        if char == '"': quote_count += 1
        if char == '#': break
        if char in ignore_tokens and quote_count % 2 == 0:
            continue

        if char in separators and quote_count % 2 == 0:
            if current_token not in [' ', '\n']:
                tokens.append(current_token)
            if char not in [' ', '\n']:
                tokens.append(char)

            current_token = ''
        else: current_token += char

    return tokens

def order_tokens(tokens):

    """
    如果当前token+kw_in_statement在all keyword string里，kw_in_statement += token
    如果当前token+kw_in_statement不在在all keyword string里，将当前kw_in_statement加到final_token里
    如果statement结束，将kw_in_statement加到final_token里
    """
    final_token = []
    kw_in_statement = ''
    temp = False
    for tok in tokens:
        if tok in all_keyword_string and kw_in_statement + tok in all_keyword_string:
            kw_in_statement += tok

        else:
            temp = True
            final_token.append(kw_in_statement)
            kw_in_statement = ''
            final_token.append(tok)

    if not temp:
        final_token.append(kw_in_statement)
    return final_token
