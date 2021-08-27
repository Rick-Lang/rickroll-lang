from PublicVariables import *
from Lexer import Lexer


# Token types
TT_keyword  = 'KEYWORDS'
TT_operator = 'OPERATORS'
TT_number   = 'VALUE-NUMBER'
TT_bool     = 'VALUE-BOOL'
TT_string   = 'VALUE-STRING'
TT_list     = 'VALUE-LIST'

TT_arguments = 'ARGUMENTS'
TT_operator = 'OPERATOR'
TT_variable = 'VARIABLE'
TT_function = 'FUNCTION'
TT_library  = 'LIBRARY'
TT_build_in_funcs = 'BUILD-IN-FUNCS'


# Keywords can execute outside main function
kw_exe_outside_main = {KW_main, KW_def1, KW_import1}

variables = []
functions = []

indent_count = 0                       # Determine if needs to indent
current_line = 0

is_main = False                        # Is the current statement in main
is_function = False                    # Is the current statement in a function


# Python source code, translated from RickRoll source code
py_code = ""

libraries = {}

# Determine variable types
def v_types(string):
    string = str(string)
    # Boolean
    if string == 'True' or string == 'False':
        return 'bool'
    # String
    if string[0] == '"' and string[-1] == '"':
        return 'string'
    # List
    if string[0] == '[' and string[-1] == ']':
        return 'list'
    # Determine the string is int or float
    count = 0
    for char in string:
        if char in digits:
            count += 1
    if count == len(string) and string.count('.') < 2:
        return 'number'

####################################################################################
'Token Class'
####################################################################################
class Token:    # Return token types
    def __init__(self, tokens):
        self.t_types = []
        self.t_values = []
        self.__tokens = tokens
        self.last_kw = ''

        for tok in self.__tokens:
            if tok:
                self.__make_token(tok)

    def add_to_tokens(self, type, token):
        self.t_types.append(type)
        self.t_values.append(token)

    def __make_token(self, tok):
        global variables, functions

        if tok in keywords:
            self.add_to_tokens(TT_keyword, tok)
            self.last_kw = tok
        elif tok in OP_build_in_functions:
            if tok == 'length': self.add_to_tokens(TT_build_in_funcs, 'len')
            if tok == 'to_string': self.add_to_tokens(TT_build_in_funcs, 'str')
            if tok == 'to_int': self.add_to_tokens(TT_build_in_funcs, 'int')
            if tok == 'to_float': self.add_to_tokens(TT_build_in_funcs, 'float')

        # Variable types
        elif v_types(tok) == 'bool':
            self.add_to_tokens(TT_bool, tok)
        elif v_types(tok) == 'string':
            self.add_to_tokens(TT_string, tok)
        elif v_types(tok) == 'list':
            self.add_to_tokens(TT_list, tok)
        elif v_types(tok) == 'number':
            self.add_to_tokens(TT_number, tok)

        # Operators
        elif tok in OP_arithmetic or tok in OP_relational or tok in OP_assignment or tok in OP_other:
            if tok == 'is': self.add_to_tokens(TT_operator, '==')
            elif tok == 'is_not': self.add_to_tokens(TT_operator, '!=')
            elif tok == 'is_greater_than': self.add_to_tokens(TT_operator, '>')
            elif tok == 'is_less_than': self.add_to_tokens(TT_operator, '<')
            else: self.add_to_tokens(TT_operator, tok)

        # Variables
        elif self.last_kw == KW_let:
            variables.append(tok)
            self.add_to_tokens(TT_variable, tok)
        # Functions
        elif self.last_kw == KW_def1:
            functions.append(tok)
            self.add_to_tokens(TT_function, tok)
        elif tok and tok in variables:
            self.add_to_tokens(TT_variable, tok)

        else:
            self.add_to_tokens(TT_arguments, tok)
            # error(f'Exception in line {current_line}: the token [{tok}] is invalid...\n')



####################################################################################
'Translate To Python'
####################################################################################

class TranslateToPython:

    def __init__(self, types, values):

        # types of the tokens
        self.types = types
        # tokens
        self.values = values

        # if there is code in the current line of code
        if self.types:

            if self.types[0] == TT_keyword or self.values[0] in functions or self.values[0] in libraries:
                if is_main or (is_main == False and self.values[0] in kw_exe_outside_main) or is_function:
                    # Convert RickRoll code to Python
                    self.convert(kw=self.values[0])

                else:
                    error(f'Exception in line {current_line}: [{self.values[0]}] can not be executed outside the main method\n')

            else:
                error(f'Exception in line {current_line}: [{self.values[0]}] is neither a keyword nor function\n')

        # if this line doesn't have code, then write "\n"
        else:
            self.write("")


    def convert(self, kw):
        global indent_count, is_main, is_function

        if kw in functions:
            self.write(join_list(self.values))

        if kw == KW_main:
            self.write('if __name__ == "__main__":')

            is_main = True
            indent_count += 1

        if indent_count == 0:
            if is_main: is_main = False
            if is_function: is_function = False

        if kw == KW_print:
            """
                print EXPR
            """

            EXPR = join_list(self.values[1:])
            self.write(f'print({EXPR}, end="")')

        if kw == KW_let:
            """
                let ID up EXPR
            """

            ID = self.values[1]
            EXPR = join_list(self.values[3:])
            self.write(f'{ID} = {EXPR}')

        if kw == KW_if:
            """
                if CONDI
            """

            CONDI = join_list(self.values[1:])
            self.write(f'if {CONDI}:')
            indent_count += 1

        if kw == KW_endless_loop:
            self.write('while True:')
            indent_count += 1

        if kw == KW_while_loop:
            """
                while1 CONDI while2
            """

            CONDI = join_list(self.values[1:])
            self.write(f'while {CONDI}:')
            indent_count += 1

        if kw == KW_break:
            self.write('break')

        if kw == KW_continue:
            self.write('continue')

        if kw == KW_def1:
            """
                def1 ID ARGS def2
            """
            ID = self.values[1]
            ARGS = join_list(self.values[2 :-1])

            self.write(f'def {ID}({ARGS}):')

            is_function = True
            indent_count += 1

        if kw == KW_return1:
            """
                return1 EXPR return2
            """
            EXPR = join_list(self.values[1: -1])
            self.write(f'return {EXPR}')

        if kw == KW_end:
            self.write('pass')
            indent_count -= 1


    def write(self, stmt):
        global py_code
        py_code += f"{'  ' * indent_count + stmt}\n"


def run_in_py(src_file_name):
    global current_line

    with open(src_file_name, mode='r', encoding='utf-8') as src:

        content = src.readlines()
        content[-1] += '\n'

        for statement in content:  # "statement" is a line of code the in source code
            current_line += 1

            lexer = Lexer(statement)
            token = Token(lexer.tokens)
            TranslateToPython(types=token.t_types, values=token.t_values)

    return py_code
