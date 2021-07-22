from os import system
from platform import system as os_name

from PublicVariables import *


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

TT_arithmetic_op = 'OP-Arithmetic'
TT_relational_op = 'OP-Relational'
TT_assignment_op = 'OP-Assignment'
TT_other_op      = 'OP-Other'

TT_variable   = 'VARIABLE'
TT_function   = 'FUNCTION'

c_separators = {
    '(', ')', '{', '}', ',', '\n', ' ', '+', '-', '*', '/', '%', '^', '='
}

variables = []
functions = []

current_line = 0


# RickRoll-Lang API in C++
API_Length = """int Length(int arr){
    return sizeof arr / sizeof arr[0];
}

"""

# C++ source code, translated from RickRoll source code
c_code = '#include<iostream>\nusing namespace std;\n'


# "join_list" is a replacement of ''.join()

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
Token class is used to tokenize a RickRoll statement
"""
####################################################################################
class Token:
    def __init__(self, statement):
        self.statement = statement
        self.tokens = []

        self.tokenize(self.statement)
        self.t_types = []
        self.t_values = []

        self.last_kw = ''

        for tok in self.tokens:
            if tok:
                self.make_token(tok)


    # Split statements to single word / token
    def tokenize(self, statement):
        current_token = ''
        quote_count = 0
        sq_bracket = 0
        for char in statement:

            if char == '[': sq_bracket += 1
            if char == ']': sq_bracket -= 1
            if char == '"': quote_count += 1
            if char == '#': break
            if char in ignore_tokens: continue

            if char in c_separators and quote_count % 2 == 0 and sq_bracket == 0:
                if current_token != ' ' and current_token != '\n':
                    self.tokens.append(current_token)
                if char != ' ' and char != '\n':
                    self.tokens.append(char)

                current_token = ''
            else: current_token += char

    def make_token(self, tok):
        def add_to_tokens(type, token):
            self.t_types.append(type)
            self.t_values.append(token)

        global variables
        global functions


        if tok in keywords:
            add_to_tokens(TT_keyword, tok)
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
        elif tok in OP_arithmetic:
            add_to_tokens(TT_arithmetic_op, tok)
        elif tok in OP_relational:
            add_to_tokens(TT_relational_op, tok)
        elif tok in OP_assignment:
            add_to_tokens(TT_assignment_op, tok)
        elif tok in OP_other:
            add_to_tokens(TT_other_op, tok)

        # Variables
        elif self.last_kw == KW_let:
            variables.append(tok)
            add_to_tokens(TT_variable, tok)
        # Functions
        elif self.last_kw == KW_def1:
            functions.append(tok)
            add_to_tokens.append(TT_function, tok)
        elif tok and tok in variables:
            add_to_tokens(TT_variable, tok)

        else:
            error(f'Exception in line {current_line}: the token [{tok}] is invalid...\n')

####################################################################################
'Translate To C++'
####################################################################################
class TranslateToCpp:
    def __init__(self, types, values):
        self.types = types
        self.values = values

        if self.types[0] == TT_keyword or self.values[0] in functions:
            # Convert RickRoll code to Cpp
            self.convert(kw=self.values[0])

        else:
            error(f'Exception in line {current_line}: [{self.values[0]}] is neither a keyword nor function\n')

    # Convert RickRoll tokens to C++
    def convert(self, kw):
        if kw in functions:
            self.write(join_list(self.values))

        if kw == KW_main:
            self.write('int main(int argc, char* argv[]){')
        if kw == KW_print:
            """
            cout << EXPR;
            """
            EXPR = join_list(self.values[1:])
            self.write(f'cout<<{EXPR};')
        if kw == KW_if:
            """
            if(CONDI){
            """
            CONDI = join_list(self.values[1:])
            self.write(f'if({EXPR})' + '{')
        if kw == KW_let:
            """
            TYPE ID = EXPR;
            """
            TYPE = ''
            ID = ''
            EXPR = ''

            exp_start_index = 0
            for i in range(len(self.types)):
                if self.types[i] == TT_variable:
                    ID = self.values[i]
                if self.values[i] == '=':
                    exp_start_index = i + 1

            EXPR = join_list(self.values[exp_start_index:])

            if v_types(eval("'" + EXPR + "'")) == 'string':
                TYPE = 'string'
            if v_types(eval(EXPR)) == 'int':
                TYPE = 'int'
            if v_types(eval(EXPR)) == 'float':
                TYPE = 'float'

            self.write(f'{TYPE} {ID}={EXPR};')

        if kw == KW_endless_loop:
            self.write('while(true){')

        if kw == KW_while_loop:
            """
            while(CONDI){
            """
            CONDI = join_list(self.values[1:])
            self.write(f'while({EXPR})' + '{')

        if kw == KW_break:
            self.write('break;')

        if kw == KW_continue:
            self.write('continue;')

        if kw == KW_def1:
            """
            int ID(ARGS){
            """
            pass
        if kw == KW_return1:
            """
            return EXPR;
            """
            EXPR = join_list(self.values[1:])
            self.write(f'return {EXPR};')

        if kw == KW_end:
            self.write('}')

    # Write to C++ code
    def write(self, content):
        global c_code
        c_code += f'{content}\n'


####################################################################################
'Main'
####################################################################################

def run_in_cpp(src_file_name):
    global current_line

    with open(src_file_name, mode='r', encoding='utf-8') as src:

        content = src.readlines()
        content[-1] += '\n'

        for statement in content:  # "statement" is a line of code the in source code
            current_line += 1

            obj = Token(statement)
            if obj.t_types:
                TranslateToCpp(types=obj.t_types, values=obj.t_values)


    f_name = src_file_name.split('.')
    f_name = join_list(f_name[0:len(f_name) - 1])

    with open(f_name + '.cpp', 'w', encoding='utf-8') as f:
        f.write(c_code)

    if os_name() == 'Windows':
        exe_file = f'{f_name}.exe'
        system(f'g++ {f_name + ".cpp"} -o {exe_file}')
        system(f'{exe_file}')

    if os_name() == 'Linux':
        exe_file = f'{f_name}.out'
        system(f'g++ {f_name + ".cpp"} -o {exe_file}')
        system(f'./{exe_file}')
