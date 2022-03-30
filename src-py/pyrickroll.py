from Keywords import *
from Lexer import lexicalize

# Token types
TT_keyword  = 'KEYWORDS'
TT_operator = 'OPERATORS'
TT_number   = 'VALUE-NUMBER'
TT_bool     = 'VALUE-BOOL'
TT_string   = 'VALUE-STRING'
TT_list     = 'VALUE-LIST'

TT_arguments = 'ARGUMENTS'
TT_variable = 'VARIABLE'
TT_function = 'FUNCTION'
TT_library  = 'LIBRARY'
TT_build_in_funcs = 'BUILD-IN-FUNCS'


# Keywords can execute outside main function
kw_exe_outside_main = {KW_main, KW_def, KW_import1}

variables = []
functions = []

current_line = 0

# Python source code, translated from RickRoll source code
py_code = ""

libraries = {}

# Determine variable types
def v_types(string):
    string = str(string)
    # Boolean
    if string in {'True', 'False'}:
        return 'bool'
    # String
    if string[0] == '"' and string[-1] == '"':
        return 'string'
    # List
    if string[0] == '[' and string[-1] == ']':
        return 'list'
    # Determine the string is int or float
    count = sum(char in digits for char in string)
    if count == len(string) and string.count('.') < 2:
        return 'number'

class Token:
    def __init__(self, tokens):
        self.t_types = []
        self.t_values = []
        self.last_kw = ''

        for tok in tokens:
            if tok:
                self.__make_token(tok)

    def add_to_tokens(self, type, token):
        self.t_types.append(type)
        self.t_values.append(token)

    def __make_token(self, tok):
        global variables, functions

        if tok in keywords:
            if tok == 'is': self.add_to_tokens(TT_operator, '==')
            elif tok == 'isnot': self.add_to_tokens(TT_operator, '!=')
            elif tok == 'isgreaterthan': self.add_to_tokens(TT_operator, '>')
            elif tok == 'islessthan': self.add_to_tokens(TT_operator, '<')
            elif tok == 'isgreaterthanorequalto': self.add_to_tokens(TT_operator, '>=')
            elif tok == 'islessthanorequalto': self.add_to_tokens(TT_operator, '<=')
            else: self.add_to_tokens(TT_keyword, tok)

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
        elif tok in operators:
            self.add_to_tokens(TT_operator, tok)

        # Variables
        elif self.last_kw == KW_let:
            variables.append(tok)
            self.add_to_tokens(TT_variable, tok)
        # Functions
        elif self.last_kw == KW_def:
            functions.append(tok)
            self.add_to_tokens(TT_function, tok)
        elif tok and tok in variables:
            self.add_to_tokens(TT_variable, tok)

        else:
            self.add_to_tokens(TT_arguments, tok)


class TranslateToPython:

    def __init__(self):
        # types of the tokens
        self.types = []
        # tokens
        self.values = []
        self.is_main = False
        self.is_function = False
        self.indent_count = 0

    def translate(self, types, values):
        self.types = types
        self.values = values
        # if there is no code in the current line of code
        if not self.types:
            self.write("")
            return
        if not (self.types[0] == TT_keyword or self.values[0] in functions or self.values[0] in libraries):
            stdout.write(f'Exception in line {current_line}: [{self.values[0]}] is neither a keyword nor function\n')
            return

        if self.is_main or (self.is_main == False and self.values[0] in kw_exe_outside_main) or self.is_function:
            # Convert Rickroll code to Python
            self.convert(kw=self.values[0])

        else:
            stdout.write(f'Exception in line {current_line}: [{self.values[0]}] can not be executed outside the main method\n')


    def convert(self, kw):

        if kw in functions:
            self.write(join_list(self.values))

        elif kw == KW_main:
            self.write('if __name__ == "__main__":')

            self.is_main = True
            self.indent_count += 1

        elif self.indent_count == 0:
            self.is_main = False
            self.is_function = False

        elif kw == KW_print:
            """
                print EXPR
            """

            EXPR = join_list(self.values[1:])
            self.write(f'print({EXPR}, end="")')

        elif kw == KW_let:
            """
                let ID up EXPR
            """

            ID = join_list(self.values[self.values.index(KW_let) + 1 : self.values.index(KW_assign)])
            EXPR = join_list(self.values[self.values.index(KW_assign) + 1:])
            self.write(f'{ID} = {EXPR}')

        elif kw == KW_if:
            """
                if CONDI
            """

            CONDI = join_list(self.values[1:])
            self.write(f'if {CONDI}:')
            self.indent_count += 1

        elif kw == KW_try:
            self.write('try:')
            self.indent_count += 1

        elif kw == KW_except:
            self.write('except:')
            self.indent_count += 1

        elif kw == KW_endless_loop:
            self.write('while True:')
            self.indent_count += 1

        elif kw == KW_while_loop:
            """
                while1 CONDI
            """

            CONDI = join_list(self.values[1:])
            self.write(f'while {CONDI}:')
            self.indent_count += 1

        elif kw == KW_break:
            self.write('break')

        elif kw == KW_continue:
            self.write('continue')

        elif kw == KW_def:
            """
                def ID ARGS
            """
            ID = self.values[1]
            ARGS = join_list(self.values[2:])

            self.write(f'def {ID}({ARGS}):')

            self.is_function = True
            self.indent_count += 1

        elif kw == KW_return1:
            """
                return1 EXPR return2
            """
            EXPR = "".join(self.values[1:])
            self.write(f'return {EXPR}')

        elif kw == KW_end:
            self.write('pass')
            self.indent_count -= 1


    def write(self, stmt):
        global py_code
        py_code += f"{'  ' * self.indent_count + stmt}\n"


def run_in_py(src_file_name):
    global current_line

    transpiler = TranslateToPython()

    with open(src_file_name, mode='r', encoding='utf-8') as src:

        content = src.readlines()
        content[-1] += '\n'

        for statement in content:  # "statement" is a line of code the in source code
            current_line += 1

            token = Token(lexicalize(statement))
            transpiler.translate(types=token.t_types, values=token.t_values)

    return py_code
