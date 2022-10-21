from typing import Final
from os import system
from os.path import splitext
from sys import platform

from Keywords import *
from Lexer import lexicalize
from helpers import join_list, starts_ends

class TT(Enum):
    """Token types"""
    keyword        = 'KEYWORDS'
    operator       = 'OPERATORS'
    build_in_funcs = 'Build-In-Function'
    int            = 'VALUE-Int'
    float          = 'VALUE-Float'
    bool           = 'VALUE-Bool'
    char           = 'VALUE-Char'
    string         = 'VALUE-String'
    list           = 'VALUE-List'

    arguments = 'ARGUMENTS'
    variable   = 'VARIABLE'
    function   = 'FUNCTION'

c_separators: Final = {
    '(', ')', '{', '}', ',', '\n', ' ', '+', '-', '*', '/', '%', '^', '='
}

variables: Final[list[str]] = []
declared_variables: Final[set[str]] = set()
functions: Final[list[str]] = []

current_line = 0

c_code = '''#include<iostream>
using namespace std;
int length(int arr[]){
    return sizeof(arr) / sizeof(arr[0]);
}\n'''
"""C++ source code, translated from RickRoll source code"""

def v_types(s: str):
    """Determine var type from literal-syntax"""
    # Boolean
    if s in {'True', 'False'}:
        return 'bool'
    # String
    if starts_ends(s, '"'):
        return 'string'
    # List or Array
    if s[0] == '[' and s[-1] == ']':
        return 'list'
    # Determine the string is int or float
    count = 0
    dot_count = 0
    for char in s:
        if char in digits:
            count += 1
        if char == '.':
            dot_count += 1
    if count == len(s):
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
        # named `_type` to avoid collision with built-in `type`
        def add_to_tokens(_type: str, tok: str):
            self.t_types.append(_type)
            self.t_values.append(tok)

        global variables, functions

        TOK_TO_OP: Final = {
            'is': '==',
            'isnot': '!=',
            'isgreaterthan': '>',
            'islessthan': '<',
            'isgreaterthanorequalto': '>=',
            'islessthanorequalto': '<='
        }

        if tok in keywords:
            add_to_tokens(TT.operator.value, TOK_TO_OP.get(tok, tok))

            self.last_kw = tok
        elif tok in OP_build_in_functions:
            add_to_tokens(TT.build_in_funcs.value, tok)

        # Variable types
        elif v_types(tok) == 'bool':
            add_to_tokens(TT.bool.value, tok)
        elif v_types(tok) == 'string':
            add_to_tokens(TT.string.value, tok)
        elif v_types(tok) == 'list':
            tok = '{' + str(tok[1 : len(tok) -1]) + '}'
            add_to_tokens(TT.list.value, tok)
        elif v_types(tok) == 'float':
            add_to_tokens(TT.float.value, tok)
        elif v_types(tok) == 'int':
            add_to_tokens(TT.int.value, tok)

        # Operators
        elif tok in operators:
            add_to_tokens(TT.operator.value, tok)

        # Variables
        elif self.last_kw == KW.LET.value:
            variables.append(tok)
            add_to_tokens(TT.variable.value, tok)
        # Functions
        elif self.last_kw == KW.DEF.value:
            functions.append(tok)
            add_to_tokens(TT.function.value, tok)
        elif tok and tok in variables:
            add_to_tokens(TT.variable.value, tok)

        else:
            add_to_tokens(TT.arguments.value, tok)

####################################################################################
'Translate To C++'
####################################################################################
class TranslateToCpp:
    def __init__(self, types: list[str], values: list[str]):
        self.types = types
        self.values = values

        if self.types[0] == TT.keyword.value or self.values[0] in functions:
            self.convert(kw=self.values[0])

        else:
            raise SyntaxError(f'Exception in line {current_line}: [{self.values[0]}] is neither a keyword nor function\n')

    def convert(self, kw: str):
        """Convert RickRoll tokens to C++"""
        if kw in functions:
            self.write(join_list(self.values))

        if kw == KW.MAIN.value:
            self.write('int main(int argc, char* argv[]){')
        if kw == KW.PRINT.value:
            """
            cout << xpr;
            """
            xpr = join_list(self.values[1:])
            self.write(f'cout<<{xpr};')
        if kw == KW.IF.value:
            """
            if(cond){
            """
            cond = join_list(self.values[1:])
            self.write(f'if({cond})' + '{')
        if kw == KW.LET.value:
            """
            give id up xpr;
            """
            id = self.values[1]
            xpr = join_list(self.values[self.values.index('up') + 1:])

            if id not in declared_variables:
                self.write(f'auto {id}={xpr};')
                declared_variables.add(id)
            else:
                self.write(f'{id}={xpr};')

        if kw == KW.ENDLESS_LOOP.value:
            self.write('while(true){')

        if kw == KW.WHILE_LOOP.value:
            """
            while(cond){
            """
            cond = join_list(self.values[1:])
            self.write(f'while({cond})' + '{')

        if kw == KW.BREAK.value:
            self.write('break;')

        if kw == KW.CONTINUE.value:
            self.write('continue;')

        if kw == KW.DEF.value:
            """
            int id(ARGS){
            """
            id = self.values[1]
            ARGS: Final = ", ".join(["auto "+x for x in self.values[2:]])

            self.write(f"auto {id} = []({ARGS}) {{")

        if kw == KW.RETURN1.value:
            """
            return xpr;
            """
            xpr = join_list(self.values[1:])
            self.write(f'return {xpr};')

        if kw == KW.END.value:
            self.write('};')

    def write(self, content: str):
        """Write to C++ code"""
        global c_code
        c_code += f'{content}\n'


####################################################################################
'Main'
####################################################################################


def run_in_cpp(src_file_name: str):
    global current_line

    with open(src_file_name, mode='r', encoding='utf-8') as src:

        content = src.readlines()
        if len(content) > 0:
            content[-1] += '\n'

        # `statement`` is a line of code in the source code
        for statement in content:
            current_line += 1

            tokens = lexicalize(statement)
            tok = Token(tokens)
            if tok.t_types:
                TranslateToCpp(types=tok.t_types, values=tok.t_values)

    f_name: Final = splitext(src_file_name)[0]

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
