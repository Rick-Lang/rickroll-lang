from os import system
from sys import platform

from Keywords import *
from Lexer import lexicalize
from helpers import join_list, remove_file_ext


# Token types
TT_keyword        = 'KEYWORDS'
TT_operator       = 'OPERATORS'
TT_build_in_funcs = 'Build-In-Function'
TT_int            = 'VALUE-Int'
TT_float          = 'VALUE-Float'
TT_bool           = 'VALUE-Bool'
TT_char           = 'VALUE-Char'
TT_string         = 'VALUE-String'
TT_list           = 'VALUE-List'

TT_arguments = 'ARGUMENTS'
TT_variable   = 'VARIABLE'
TT_function   = 'FUNCTION'

c_separators = {
    '(', ')', '{', '}', ',', '\n', ' ', '+', '-', '*', '/', '%', '^', '='
}

variables: list[str] = []
declared_variables: set[str] = set()
functions: list[str] = []

current_line = 0

# C++ source code, translated from RickRoll source code
c_code = '''#include<iostream>
using namespace std;
int length(int arr[]){
    return sizeof(arr) / sizeof(arr[0]);
}
'''


# Determine variable types
def v_types(string: str):
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
    count = 0
    dot_count = 0
    for char in string:
        if char in digits:
            count += 1
        if char == '.':
            dot_count += 1
    if count == len(string):
        if dot_count == 1: return 'float'
        if dot_count == 0: return 'int'


####################################################################################
"""
Token
"""
####################################################################################
class Token:
    def __init__(self, raw_tokens: list[str]):
        self.t_types: list[str] = []
        self.t_values: list[str] = []

        self.last_kw = ''

        for tok in raw_tokens:
            if tok:
                self.make_token(tok)

    def make_token(self, tok: str):
        def add_to_tokens(type: str, token: str):
            self.t_types.append(type)
            self.t_values.append(token)

        global variables, functions

        TOK_TO_OP = {
            'is': '==',
            'isnot': '!=',
            'isgreaterthan': '>',
            'islessthan': '<',
            'isgreaterthanorequalto': '>=',
            'islessthanorequalto': '<='
        }

        if tok in keywords:
            add_to_tokens(TT_operator, TOK_TO_OP.get(tok, tok))

            self.last_kw = tok
        elif tok in OP_build_in_functions:
            add_to_tokens(TT_build_in_funcs, tok)

        # Variable types
        elif v_types(tok) == 'bool':
            add_to_tokens(TT_bool, tok)
        elif v_types(tok) == 'string':
            add_to_tokens(TT_string, tok)
        elif v_types(tok) == 'list':
            tok = '{' + str(tok[1 : len(tok) -1]) + '}'
            add_to_tokens(TT_list, tok)
        elif v_types(tok) == 'float':
            add_to_tokens(TT_float, tok)
        elif v_types(tok) == 'int':
            add_to_tokens(TT_int, tok)

        # Operators
        elif tok in operators:
            add_to_tokens(TT_operator, tok)

        # Variables
        elif self.last_kw == KW.LET.value:
            variables.append(tok)
            add_to_tokens(TT_variable, tok)
        # Functions
        elif self.last_kw == KW.DEF.value:
            functions.append(tok)
            add_to_tokens(TT_function, tok)
        elif tok and tok in variables:
            add_to_tokens(TT_variable, tok)

        else:
            add_to_tokens(TT_arguments, tok)

####################################################################################
'Translate To C++'
####################################################################################
class TranslateToCpp:
    def __init__(self, types: list[str], values: list[str]):
        self.types = types
        self.values = values

        if self.types[0] == TT_keyword or self.values[0] in functions:
            # Convert RickRoll code to Cpp
            self.convert(kw=self.values[0])

        else:
            raise SyntaxError(f'Exception in line {current_line}: [{self.values[0]}] is neither a keyword nor function\n')

    # Convert RickRoll tokens to C++
    def convert(self, kw: str):
        if kw in functions:
            self.write(join_list(self.values))

        if kw == KW.MAIN.value:
            self.write('int main(int argc, char* argv[]){')
        if kw == KW.PRINT.value:
            """
            cout << EXPR;
            """
            EXPR = join_list(self.values[1:])
            self.write(f'cout<<{EXPR};')
        if kw == KW.IF.value:
            """
            if(CONDI){
            """
            CONDI = join_list(self.values[1:])
            self.write(f'if({CONDI})' + '{')
        if kw == KW.LET.value:
            """
            give ID up EXPR;
            """
            ID = self.values[1]
            EXPR = join_list(self.values[self.values.index('up') + 1:])

            if ID not in declared_variables:
                self.write(f'auto {ID}={EXPR};')
                declared_variables.add(ID)
            else:
                self.write(f'{ID}={EXPR};')

        if kw == KW.ENDLESS_LOOP.value:
            self.write('while(true){')

        if kw == KW.WHILE_LOOP.value:
            """
            while(CONDI){
            """
            CONDI = join_list(self.values[1:])
            self.write(f'while({CONDI})' + '{')

        if kw == KW.BREAK.value:
            self.write('break;')

        if kw == KW.CONTINUE.value:
            self.write('continue;')

        if kw == KW.DEF.value:
            """
            int ID(ARGS){
            """
            ID = self.values[1]
            ARGS = ", ".join(["auto "+x for x in self.values[2:]])

            self.write(f"auto {ID} = []({ARGS}) {{")

        if kw == KW.RETURN1.value:
            """
            return EXPR;
            """
            EXPR = join_list(self.values[1:])
            self.write(f'return {EXPR};')

        if kw == KW.END.value:
            self.write('};')

    # Write to C++ code
    def write(self, content: str):
        global c_code
        c_code += f'{content}\n'


####################################################################################
'Main'
####################################################################################


def run_in_cpp(src_file_name: str):
    global current_line

    with open(src_file_name, mode='r', encoding='utf-8') as src:

        content = src.readlines()
        content[-1] += '\n'

        for statement in content:  # "statement" is a line of code in the source code
            current_line += 1

            tokens = lexicalize(statement)
            tok = Token(tokens)
            if tok.t_types:
                TranslateToCpp(types=tok.t_types, values=tok.t_values)

    f_name = remove_file_ext(src_file_name)

    with open(f'{f_name}.cpp', 'w+', encoding='utf-8') as f:
        f.write(c_code)

    if platform == 'win32':
        exe_file = f'{f_name}.exe'
        system(f'g++ {f_name}.cpp -o {exe_file}')
        system(f'{exe_file}')
    elif platform == 'linux':
        exe_file = f'{f_name}.out'
        system(f'g++ {f_name}.cpp -o {exe_file}')
        system(f'./{exe_file}')
    else:
        raise NotImplementedError(f"Platform {platform} is not supported")
