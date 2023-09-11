from typing import Final
from os import system
from os.path import splitext
from sys import platform

from Keywords import *
from Lexer import lexicalize
from helpers import join_list, starts_ends

class TT(Enum):
    """Token types"""
    KEYWORD        = 'KEYWORDS'
    OPERATOR       = 'OPERATORS'
    BUILD_IN_FUNCS = 'Build-In-Function'
    INT            = 'VALUE-Int'
    FLOAT          = 'VALUE-Float'
    BOOL           = 'VALUE-Bool'
    CHAR           = 'VALUE-Char'
    STRING         = 'VALUE-String'
    LIST           = 'VALUE-List'

    ARGUMENTS = 'ARGUMENTS'
    VARIABLE   = 'VARIABLE'
    FUNCTION   = 'FUNCTION'

c_separators: Final = set('(){},\n +-*/%^=')

variables: Final[list[str]] = []
declared_variables: Final[set[str]] = set()
functions: Final[list[str]] = []

current_line = 0


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
        if char in DIGITS:
            count += 1
        if char == '.':
            dot_count += 1
    if count == len(s):
        if dot_count == 1: return 'float'
        if dot_count == 0: return 'int'


####################################################################################
'Token'
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

        if tok in KEYWORDS:
            add_to_tokens(TT.OPERATOR.value, TOK_TO_OP.get(tok, tok))

            self.last_kw = tok
        elif tok in OP_BUILT_IN_FUNCTIONS:
            add_to_tokens(TT.BUILD_IN_FUNCS.value, tok)

        # Variable types
        elif v_types(tok) == 'bool':
            add_to_tokens(TT.BOOL.value, tok)
        elif v_types(tok) == 'string':
            add_to_tokens(TT.STRING.value, tok)
        elif v_types(tok) == 'list':
            tok = '{' + str(tok[1 : len(tok) -1]) + '}'
            add_to_tokens(TT.LIST.value, tok)
        elif v_types(tok) == 'float':
            add_to_tokens(TT.FLOAT.value, tok)
        elif v_types(tok) == 'int':
            add_to_tokens(TT.INT.value, tok)

        # Operators
        elif tok in OPERATORS:
            add_to_tokens(TT.OPERATOR.value, tok)

        # Variables
        elif self.last_kw == KW.LET.value:
            variables.append(tok)
            add_to_tokens(TT.VARIABLE.value, tok)
        # Functions
        elif self.last_kw == KW.DEF.value:
            functions.append(tok)
            add_to_tokens(TT.FUNCTION.value, tok)
        elif tok and tok in variables:
            add_to_tokens(TT.VARIABLE.value, tok)

        else:
            add_to_tokens(TT.ARGUMENTS.value, tok)

####################################################################################
'Translate To C++'
####################################################################################
c_code = '''#include<iostream>
using namespace std;
int length(int arr[]){
    return sizeof(arr) / sizeof(arr[0]);
}\n\n'''

class TranslateToCpp:
    def __init__(self):
        self.types = []
        self.values = []
        self.indent_count = 0
        self.c_code = c_code
        # if self.types[0] == TT.KEYWORD.value or self.values[0] in functions:
        #     self.convert(kw=self.values[0])

        # else:
        #     raise SyntaxError(f'Exception in line {current_line}: [{self.values[0]}] is neither a keyword nor function\n')

    def translate(self, types: list[str], values: list[str]):
        self.types = types
        self.values = values
        self.convert(kw=self.values[0])

    def convert(self, kw: str):
        """
        Convert RickRoll tokens to C++
        self.convert("takemetourheart")
        >>> "int main(int argc, char* argv[]){"

        Inside the TranslateToCPP class, self.values is used

        self.convert("ijustwannatelluhowimfeeling")
        when self.values is ["ijustwannatelluhowimfeeling", "Hello World\n"]
        >>> "cout "Hello World\n""

        """

        if kw in functions:
            self.write(join_list(self.values))
            self.indent_count += 1

        if kw == KW.MAIN.value:
            self.write('int main(int argc, char* argv[]){')
            self.indent_count += 1
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
            self.indent_count += 1
        if kw == KW.LET.value:
            """
            give id up xpr;
            """
            # named `_id` to avoid collision with `id`
            _id = self.values[1]
            xpr = join_list(self.values[self.values.index('up') + 1:])

            if _id not in declared_variables:
                self.write(f'auto {_id}={xpr};')
                declared_variables.add(_id)
            else:
                self.write(f'{_id}={xpr};')

        if kw == KW.ENDLESS_LOOP.value:
            self.write('while(true){')
            self.indent_count += 1

        if kw == KW.WHILE_LOOP.value:
            """
            while(cond){
            """
            cond = join_list(self.values[1:])
            self.write(f'while({cond})' + '{')
            self.indent_count += 1

        if kw == KW.BREAK.value:
            self.write('break;')

        if kw == KW.CONTINUE.value:
            self.write('continue;')

        if kw == KW.DEF.value:
            """
            void id(ARGS){
            """
            _id = self.values[1]
            ARGS: Final = ", ".join(["auto "+x for x in self.values[2:]])

            self.write(f"auto {_id} = []({ARGS}) {{")
            self.indent_count += 1

        if kw == KW.RETURN1.value:
            """
            return xpr;
            """
            xpr = join_list(self.values[1:])
            self.write(f'return {xpr};')

        if kw == KW.END.value:
            self.indent_count -= 1
            self.write('};')
            

    def write(self, content: str):
        """Write to C++ code"""
        
        self.c_code += f'{"    " * self.indent_count + content}\n'


####################################################################################
'Main'
####################################################################################


def run(src_file_name: str):
    global current_line

    transpiler = TranslateToCpp()

    with open(src_file_name, mode='r', encoding='utf-8') as src:

        content = src.readlines()
        if len(content) > 0:
            content[-1] += '\n'

        """
        `statement`` is a line of code in the source code
        """
        for statement in content:
            current_line += 1

            tokens = lexicalize(statement)
            tok = Token(tokens)
            if tok.t_types:
                transpiler.translate(types=tok.t_types, values=tok.t_values)

    f_name: Final = splitext(src_file_name)[0]

    with open(f'{f_name}.cpp', 'w+', encoding='utf-8') as f:
        f.write(transpiler.c_code)
    print(transpiler.c_code)

    if platform == 'win32':
        exe_file = f'{f_name}.exe'
        system(f'g++ {f_name}.cpp -o {exe_file}')
        system(f'{exe_file}')
    elif platform == 'linux':
        exe_file = f'{f_name}.out'
        system(f'g++ {f_name}.cpp -o {exe_file}')
        system(f'./{exe_file}')
    elif platform == 'darwin':
        exe_file = f'{f_name}.out'
        system(f'g++ {f_name}.cpp -o {exe_file}')
        system(f'./{exe_file}')
    else:
        raise NotImplementedError(f"Platform {platform} is not supported")
