from os import system
from platform import system as os_name

from PublicVariables import *


# Token types
TT_keyword    = 'KEYWORDS'
TT_operator   = 'OPERATORS'
TT_number     = 'VALUE-NUMBER'
TT_bool       = 'VALUE-Bool'
TT_char       = 'VALUE-Char'
TT_string     = 'VALUE-String'
TT_list       = 'VALUE-List'

TT_variable   = 'VARIABLE'
TT_function   = 'FUNCTION'


variables = []
functions = []

current_line = 0

# Python source code, translated from RickRoll source code
c_code = '#include<iostream>\nusing namespace std;\n'


# "join_list" is a replacement of ''.join()
def join_list(l):
    result = ''
    for i in l: result += str(i)
    return result


####################################################################################
"""
Token class is used to tokenize a RickRoll statement
"""
####################################################################################
class Token:
    def __init__(self, statement):
        self.statement = statement
        self.tokens = []

        self.tokenize()

        self.t_types = []
        self.t_values = []

        for i in range(len(self.tokens)):
            if self.tokens[i]:
                self.convert_token(i)



    # Split statements to single word / token
    def tokenize(self):

        current_token = ''
        quote_count = 0

        for char in self.statement:

            if char == '"':
                quote_count += 1

            if char == '#':
                break
            if char in ignore_tokens:
                continue

            if char in separators and quote_count % 2 == 0:

                if current_token != ' ' and current_token != '\n':
                    self.tokens.append(current_token)
                if char != ' ' and char != '\n':
                    self.tokens.append(char)

                current_token = ''

            else:
                current_token += char


    # is_num determines whether the token is a number
    def is_num(self, string = ''):
        count = 0
        for i in string:
            if i in digits:
                count += 1

        return True if len(string) == count and string.count('.') <= 1 else False


    # Convert each token to 
    def convert_token(self, i=0):

        global variables

        def add_to_parser(token_type):
            self.t_types.append(token_type)
            self.t_values.append(self.tokens[i])

        def add_operator(operator_in_python):
            self.t_types.append(TT_operator)
            self.t_values.append(operator_in_python)


        t = self.tokens[i]

        # If the token is a key word
        if t in keywords:
            add_to_parser(TT_keyword)


    # Operators
        # Arithmetic Operators
        elif t in OP_arithmetic or t in OP_assignment or t in OP_other:
            add_to_parser(TT_operator)

        # Relational Operator
        elif t in OP_relational or t in OP_build_in_functions:
            if t == 'is': add_operator('==')
            if t == 'is_not': add_operator('!=')
            if t == 'is_greater_than': add_operator('>')
            if t == 'is_less_than': add_operator('<')
            if t == 'and': add_operator('&&')
            if t == 'or': add_operator('||')

            # Build in functions
            if t == 'ToString': add_operator('str')
            if t == 'ToInt': add_operator('int')
            if t == 'ToFloat': add_operator('float')
            if t == 'Length': add_operator('len')


    # Value
        # number
        elif self.is_num(t):
            add_to_parser(TT_number)

        # Bool
        elif t == 'True' or t == 'False':
            add_to_parser(TT_bool)

        # String
        elif t[0] == '"' and t[-1] == '"':
            add_to_parser(TT_string)

    # Others
        # Variables / Functions
        elif self.tokens[i - 1] == KW_let:
            add_to_parser(TT_variable)
            variables.append(t)

        # Library
        elif self.tokens[i - 1] == KW_import1:
            add_to_parser(TT_library)

        elif self.tokens[i - 1] == KW_def1:
            add_to_parser(TT_function)
            functions.append(t)

        # Others and possible variables
        elif t and t in variables:
            add_to_parser(TT_variable)

        else:
            stdout.write(f'Exception in line {current_line}: the token [{t}] is invalid...\n')
            exit('------'*10 + '\n"You know the rules, and so do I~"')


####################################################################################
'Translate To C++'
####################################################################################

class TranslateToCPP:

    def __init__(self, types, values):

        self.types = types        # types of the tokens
        self.values = values      # tokens

        if self.types[0] == TT_keyword or self.values[0] in functions:
            # Convert RickRoll code to Python
            self.convert(kw=self.values[0])

        else:
            stdout.write(f'Exception in line {current_line}: [{self.values[0]}] is neither a keyword nor function\n')
            exit('------'*10 + '\n"You know the rules, and so do I~"')


    def convert(self, kw):

        if kw in functions:
            self.write(f'{join_list(self.values)}')

        if kw == KW_main:
            self.write('int main(int argc, char* argv[]){')

        if kw == KW_print:
            # print EXP

            exp = join_list(self.values[1: len(self.values)])
            self.write(f'cout<<{exp};')

        if kw == KW_let:
            # IDENTIFIER = VALUE
            exp = self.values[1: len(self.values)]

            eql_op_index = 0
            var = ''
            for i in range(len(self.types)):
                if self.values[i] == '=':
                    eql_op_index = i

                if self.types[i] == TT_variable:
                    var = self.values[i]

                if self.types[i] == TT_string:
                    self.write(f'string {var} = {join_list(exp[eql_op_index:len(exp)])};')
                    break

                if self.types[i] == TT_number:
                    self.write(f'int {var} = {join_list(exp[eql_op_index:len(exp)])};')
                    break

                if self.types[i] == TT_bool:
                    self.write(f'bool {var} = {join_list(exp[eql_op_index:len(exp)])};')
                    break


        if kw == KW_if:
            # IF CONDITION:

            condition = join_list(self.values[1: len(self.values)])
            self.write(f'if({condition})' + '{')

        if kw == KW_endless_loop:
            self.write('while(true){')

        if kw == KW_while_loop:
            condition = join_list(self.values[1: len(self.values)])
            self.write(f'while({condition})' + '{')

        if kw == KW_break:
            self.write('break;')

        if kw == KW_continue:
            self.write('continue;')

        if kw == KW_def1:
            arguments = join_list(self.values[2 : len(self.values) - 1])

            self.write(f'char {self.values[1]}({arguments})' + '{')

        if kw == KW_return1:
            exp = join_list(self.values[1: len(self.values) - 1])
            self.write(f'return {exp};')


        if kw == KW_end:
            self.write('}')


    def write(self, stmt):
        global c_code
        c_code += stmt + '\n'



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
                TranslateToCPP(types=obj.t_types, values=obj.t_values)

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

    
