from sys import argv, stdout

# Keywords

KW_print        = 'i_just_wanna_tell_u_how_im_feeling'
KW_if           = 'and_if_u_ask_me_how_im_feeling'

KW_let          = 'give_u_up'
KW_import1      = 'we_know_the'
KW_import2      = "and_we're_gonna_play_it"
KW_def1         = 'never_knew'
KW_def2         = 'could_feel_this_way'
KW_return1      = 'when_i_give_my'
KW_return2      = 'it_will_be_completely'
KW_main         = 'take_me_to_ur_heart'
KW_end          = 'say_good_bye'

KW_break        = 'desert_u'
KW_continue     = 'run_around'
KW_endless_loop = 'together_forever_and_never_to_part'
KW_while_loop   = 'together_forever_with'

keywords = {
    KW_print,
    KW_if,
    KW_let,
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
}


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

OP_build_in_functions = {'ToString', 'ToInt', 'ToFloat', 'Length'}
